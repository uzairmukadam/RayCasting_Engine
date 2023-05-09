from settings import *


class TextureRenderer:
    def __init__(self, game):
        self.game = game
        self.wall_textures = {}
        self.vert_pixels = []

        self.load_textures()

    def load_textures(self):
        res = (texture_size, texture_size)
        for wall in list(self.game.map.wall.keys()):
            path = self.game.map.wall_texture[wall]
            temp_texture = pg.image.load(path).convert_alpha()

            self.wall_textures[wall] = pg.transform.scale(temp_texture, res)

    def update(self):
        self.vert_pixels = self.game.ray_caster.columns

    def draw_floor(self):
        color = [110, 110, 110]
        pg.draw.rect(self.game.screen, color,
                     (0, (height // 2) + self.game.player.vert, width, (height // 2) - self.game.player.vert))

    def draw(self):
        #self.draw_floor()

        vertical_shift = self.game.player.vert
        for i in range(num_rays):
            pixel_column = self.vert_pixels[i]["wall"]

            drawn_height = 0

            for block in pixel_column:
                ray_length = block["ray_length"]

                projection_block_height = block["block_height"]

                temp_color = self.game.map.wall[block["wall_id"]]

                wall_height = block["wall_height"]

                projection_height = projection_block_height * wall_height

                drawing_height = height - (height // 2 - projection_block_height // 2 - projection_block_height * (
                        wall_height - 1)) - vertical_shift

                color = []

                if drawing_height > drawn_height:
                    for j in range(3):
                        color.append(temp_color[j] * (1 - (ray_length / max_depth)))

                    visible_height = drawing_height - drawn_height

                    if visible_height > projection_height:
                        visible_height = projection_height

                    pg.draw.rect(self.game.screen, color,
                                 (i * scale,
                                  height - drawing_height,
                                  scale,
                                  visible_height))

                    drawn_height = drawing_height
