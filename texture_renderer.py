from settings import *


class TextureRenderer:
    def __init__(self, game):
        self.game = game
        self.wall_textures = {}
        self.vert_pixels = []
        self.vert_scanlines = []

        self.load_textures()

    def load_textures(self):
        res = (texture_size, texture_size)
        for wall in list(self.game.map.wall.keys()):
            path = self.game.map.wall_texture[wall]
            temp_texture = pg.image.load(path).convert_alpha()

            self.wall_textures[wall] = pg.transform.scale(temp_texture, res)

    def update(self):
        self.vert_scanlines = []
        self.vert_pixels = self.game.ray_caster.columns
        player_pos = self.game.player.pos
        for column in self.vert_pixels:
            ray_angle = column["ray_angle"]
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            wall_offset = []
            for block in column["wall"]:
                texture_offset = 0
                ray_length = block["ray_length"]

                if (player_pos[0] + (ray_length * cos_a)) % block_size == 0:
                    y_offset = ((player_pos[1] + (ray_length * sin_a)) % block_size)
                    texture_offset = y_offset * (texture_size - 1)
                elif (player_pos[1] + (ray_length * sin_a)) % block_size == 0:
                    x_offset = ((player_pos[0] + (ray_length * cos_a)) % block_size)
                    texture_offset = (1 - x_offset) * (texture_size - 1)

                wall_offset.append(texture_offset)
            self.vert_scanlines.append(wall_offset)

    def draw_floor(self):
        color = [110, 110, 110]
        pg.draw.rect(self.game.screen, color,
                     (0, (height // 2) + self.game.player.vert, width, (height // 2) - self.game.player.vert))

    def draw(self):
        # self.draw_floor()

        vertical_shift = self.game.player.vert
        for i in range(len(self.vert_pixels)):
            pixel_column = self.vert_pixels[i]

            drawn_height = 0
            for j in range(len(pixel_column["wall"])):
                block = pixel_column["wall"][j]
                ray_length = block["ray_length"]
                projection_block_height = block["block_height"]
                wall_height = block["wall_height"]
                projection_height = projection_block_height * wall_height
                texture_id = block["wall_id"]
                offset = self.vert_scanlines[i][j]

                drawing_height = height - (height // 2 - projection_block_height // 2 - projection_block_height * (
                        wall_height - 1)) - vertical_shift

                if drawing_height > drawn_height:

                    color = []
                    temp_color = [255, 255, 255]
                    for channel in range(3):
                        color.append(temp_color[channel] * (1 - (ray_length / max_depth)))

                    visible_height = drawing_height - drawn_height

                    if visible_height > projection_height:
                        visible_height = projection_height

                    wall_column = self.wall_textures[texture_id].subsurface(offset, 0, scale, texture_size)
                    wall_column = pg.transform.scale(wall_column, (scale, projection_height))
                    wall_column.fill((color[0], color[1], color[2], 100), special_flags=pg.BLEND_MULT)

                    self.game.screen.blit(wall_column,
                                          (i * scale, height - drawing_height), (0, 0, scale, visible_height))

                    drawn_height = drawing_height
