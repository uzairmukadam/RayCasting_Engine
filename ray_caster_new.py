from settings import *


class RayCaster:
    def __init__(self, game):
        self.game = game
        self.vert_pixels = []

    def update(self):
        px, py = self.game.player.pos
        mx, my = int(px / block_size), int(py / block_size)

        self.vert_pixels = []

        ray_angle = self.game.player.angle - (fov / 2) + 0.0001

        for ray in range(num_rays):
            data = {"ray_angle": ray_angle, "ray_length": max_depth, "wall_id": 0, "proj_height": 0}
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            x_depth = (((mx + 1) * block_size) - px) if cos_a > 0 else (
                    px - (mx * block_size))

            y_depth = (((my + 1) * block_size) - py) if sin_a > 0 else (
                    py - (my * block_size))

            ray_length = 0

            d_mx = mx
            d_my = my

            while ray_length <= max_depth:
                if self.game.map.game_map[(d_mx, d_my)] in self.game.map.wall:
                    length = ray_length * math.cos(self.game.player.angle - ray_angle)
                    data["ray_length"] = ray_length
                    data["proj_height"] = (screen_distance / (length + 0.0001))
                    data["wall_id"] = self.game.map.game_map[(d_mx, d_my)]
                    break

                x_length = abs(x_depth / cos_a)
                y_length = abs(y_depth / sin_a)

                if y_length < x_length:
                    ray_length = y_length
                    y_depth += block_size
                    d_my += sin_a / abs(sin_a)
                elif y_length > x_length:
                    ray_length = x_length
                    x_depth += block_size
                    d_mx += cos_a / abs(cos_a)
                else:
                    ray_length = x_length
                    x_depth += block_size
                    y_depth += block_size
                    d_mx += cos_a / abs(cos_a)
                    d_my += sin_a / abs(sin_a)

            self.vert_pixels.append(data)
            ray_angle += delta_angle

    def draw(self):
        for i in range(num_rays):
            ray_length = self.vert_pixels[i]["ray_length"]
            ray_angle = self.vert_pixels[i]["ray_angle"]
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            px, py = self.game.player.pos
            pg.draw.line(self.game.screen, 'yellow',
                         (px * scale_2d, py * scale_2d),
                         (px * scale_2d + ray_length * scale_2d * cos_a, py * scale_2d + ray_length * scale_2d * sin_a),
                         1)

    def draw3d(self):
        vertical_shift = self.game.player.vert
        for i in range(num_rays):
            ray_length = self.vert_pixels[i]["ray_length"]
            wall_id = self.vert_pixels[i]["wall_id"]
            if ray_length != -1:
                length = ray_length * math.cos(self.game.player.angle - self.vert_pixels[i]["ray_angle"])
                projection_height = (screen_distance / (length + 0.0001))

                temp_color = self.game.map.wall_color[wall_id]

                color = []

                for j in range(3):
                    color.append(temp_color[j] * (1 - (ray_length / max_depth)))

                pg.draw.rect(self.game.screen, color,
                             (i * scale, (height // 2 - projection_height // 2) + vertical_shift, scale,
                              projection_height))