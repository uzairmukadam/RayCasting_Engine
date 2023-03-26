from settings import *
import pygame as pg
import math


class RayCaster:
    def __init__(self, game):
        self.game = game
        self.ray_length = [-1] * num_rays
        self.ray_angle = [None] * num_rays

    def update(self):
        px, py = self.game.player.pos
        mx, my = int(px / block_size), int(py / block_size)

        self.ray_length = [-1] * num_rays
        self.ray_angle = [None] * num_rays

        ray_angle = self.game.player.angle - (fov / 2) + 0.0001

        for ray in range(num_rays):
            self.ray_angle[ray] = ray_angle
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
                    self.ray_length[ray] = ray_length
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

            ray_angle += delta_angle

    def draw(self):
        for i in range(num_rays):
            ray = self.ray_length[i]
            if ray == -1:
                ray = max_depth
            ray_angle = self.ray_angle[i]
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            px, py = self.game.player.pos
            pg.draw.line(self.game.screen, 'yellow',
                         (px, py), (px + ray * cos_a, py + ray * sin_a), 1)

    def draw3d(self):
        for i in range(num_rays):
            ray_length = self.ray_length[i]
            if ray_length != -1:
                projection_height = screen_distance / (ray_length + 0.0001)
                color = [255 * (1 - (ray_length / max_depth)), 255 * (1 - (ray_length / max_depth)),
                         255 * (1 - (ray_length / max_depth))]
                pg.draw.rect(self.game.screen, color,
                             (i * scale, ((height // 2) - projection_height // 2) + self.game.player.vert,
                              scale,
                              projection_height))
