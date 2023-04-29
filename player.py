from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = self.game.map.start_block[0], self.game.map.start_block[1]
        self.angle = 0
        self.vert = 0

    def set_max_drawDist(self):
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)

        x_length = self.game.map.map_dimen[0]
        y_length = self.game.map.map_dimen[1]

        if cos_a > 0:
            x_length -= self.x
        else:
            x_length = self.x

        if sin_a < 0:
            y_length -= self.y
        else:
            y_length = self.y

        pg.draw.line(self.game.screen, 'blue',
                     (self.x * scale_2d, self.y * scale_2d),
                     (self.x * scale_2d + x_length * scale_2d,
                      self.y * scale_2d), 1)
        pg.draw.line(self.game.screen, 'red',
                     (self.x * scale_2d, self.y * scale_2d),
                     (self.x * scale_2d,
                      self.y * scale_2d + y_length * scale_2d), 1)

    def check_collision(self, dx, dy):
        if dx >= 0:
            outer_radius_x = outer_radius
        else:
            outer_radius_x = (-1) * outer_radius
        x = int((self.x + dx + outer_radius_x))
        if self.game.map.map[x, int(self.y)][0] not in list(self.game.map.wall.keys()):
            self.x += dx

        if dy >= 0:
            outer_radius_y = outer_radius
        else:
            outer_radius_y = (-1) * outer_radius
        y = int((self.y + dy + outer_radius_y))
        if self.game.map.map[int(self.x), y][0] not in list(self.game.map.wall.keys()):
            self.y += dy

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        sin_b = math.sin(self.angle + (math.pi / 2))
        cos_b = math.cos(self.angle + (math.pi / 2))

        dx, dy = 0, 0

        speed = player_speed * self.game.delta_time
        sin_speed = speed * sin_a
        cos_speed = speed * cos_a
        sin_side_speed = speed * sin_b * 0.5
        cos_side_speed = speed * cos_b * 0.5

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            dx += cos_speed
            dy += sin_speed
        if keys[pg.K_s]:
            dx -= cos_speed
            dy -= sin_speed

        if keys[pg.K_a]:
            dx -= cos_side_speed
            dy -= sin_side_speed
        if keys[pg.K_d]:
            dx += cos_side_speed
            dy += sin_side_speed

        self.check_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= rotation_speed * self.game.delta_time

        if keys[pg.K_RIGHT]:
            self.angle += rotation_speed * self.game.delta_time

        if keys[pg.K_UP]:
            if self.vert <= height // 2:
                self.vert += vertical_speed

        if keys[pg.K_DOWN]:
            if self.vert >= height // 2 * -1:
                self.vert -= vertical_speed

    def update(self):
        self.movement()

    def draw(self):
        pg.draw.circle(self.game.screen, 'green',
                       (self.x * scale_2d, self.y * scale_2d), 5)

        pg.draw.line(self.game.screen, 'red',
                     (self.x * scale_2d, self.y * scale_2d),
                     (self.x * scale_2d + draw_distance * scale_2d * math.cos(self.angle),
                      self.y * scale_2d + draw_distance * scale_2d * math.sin(self.angle)), 1)

    @property
    def pos(self):
        return self.x, self.y
