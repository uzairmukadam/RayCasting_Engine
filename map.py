import pygame as pg
from settings import *

game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Map:
    def __init__(self, game):
        self.game = game
        self.game_map = {}
        self.current_zone = 0
        self.start_block = 75, 75
        self.wall = [1]
        self.get_map()

    def get_map(self):
        for y, row in enumerate(game_map):
            for x, block in enumerate(row):
                self.game_map[(x, y)] = block

    def draw(self):
        for pos in self.game_map:
            if self.game_map[pos] in self.wall:
                pg.draw.rect(self.game.screen, 'white',
                             (pos[0] * block_size, pos[1] * block_size, block_size, block_size))
