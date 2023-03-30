import pygame as pg
from settings import *
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = self.game.map.start_block
        self.angle = 0
        self.vert = 0

    def check_collision(self, dx, dy):
        x = int((self.x + dx) / block_size)
        y = int((self.y + dy) / block_size)

        if self.game.map.game_map[(x, y)] not in self.game.map.wall:
            self.x += dx
            self.y += dy

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        dx, dy = 0, 0

        speed = player_speed * self.game.delta_time
        sin_speed = speed * sin_a
        cos_speed = speed * cos_a

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            dx += cos_speed
            dy += sin_speed
        if keys[pg.K_s]:
            dx -= cos_speed
            dy -= sin_speed

        self.check_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= rotation_speed * self.game.delta_time

        if keys[pg.K_RIGHT]:
            self.angle += rotation_speed * self.game.delta_time

    def update(self):
        self.movement()

    def draw(self):
        pg.draw.circle(self.game.screen, 'green',
                       (self.x * scale_2d, self.y * scale_2d), 5)

        pg.draw.line(self.game.screen, 'blue',
                     (self.x * scale_2d, self.y * scale_2d),
                     (self.x * scale_2d + draw_distance * scale_2d * math.cos(self.angle), self.y * scale_2d + draw_distance * scale_2d * math.sin(self.angle)), 1)

    @property
    def pos(self):
        return self.x, self.y
