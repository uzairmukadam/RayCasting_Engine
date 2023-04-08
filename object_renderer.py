from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_texture = {}
        self.vert_pixels = []

        for i in self.game.map.wall_asset:
            self.wall_texture[i] = self.get_texture(self.game.map.wall_asset[i])

    @staticmethod
    def get_texture(path, res=(texture_size, texture_size)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def update(self):
        self.vert_pixels = self.game.ray_caster.vert_pixels
        player_pos = self.game.player.pos
        player_angle = self.game.player.angle
        for i in range(len(self.vert_pixels)):
            texture_offset = 0
            ray_length = self.vert_pixels[i]["ray_length"]
            ray_angle = self.vert_pixels[i]["ray_angle"]
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            if self.vert_pixels[i]["proj_height"] != 0:

                if (player_pos[0] + (ray_length * cos_a)) % block_size == 0:
                    y_offset = ((player_pos[1] + (ray_length * sin_a)) % block_size)
                    if math.cos(player_angle - ray_angle) > 0:
                        texture_offset = y_offset * (texture_size - 1)
                    else:
                        texture_offset = (1 - y_offset) * (texture_size - 1)
                elif (player_pos[1] + (ray_length * sin_a)) % block_size == 0:
                    x_offset = ((player_pos[0] + (ray_length * cos_a)) % block_size)
                    if math.sin(player_angle - ray_angle) > 0:
                        texture_offset = (1 - x_offset) * (texture_size - 1)
                    else:
                        texture_offset = x_offset * (texture_size - 1)

            self.vert_pixels[i]["texture_offset"] = texture_offset

    def draw(self):
        for i in range(len(self.vert_pixels)):
            projection_height = self.vert_pixels[i]["proj_height"]
            texture_id = self.vert_pixels[i]["wall_id"]
            offset = self.vert_pixels[i]["texture_offset"]
            if projection_height != 0:
                wall_column = self.wall_texture[texture_id].subsurface(offset, 0, scale, texture_size)
                wall_column = pg.transform.scale(wall_column, (scale, projection_height))

                self.screen.blit(wall_column,
                                 (i * scale, (height // 2) - (projection_height // 2) + self.game.player.vert))
