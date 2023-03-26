import math

import pygame as pg


def get_window_mode(mode=0):
    modes = {
        0: pg.SHOWN,
        1: pg.NOFRAME,
        2: pg.FULLSCREEN
    }

    return modes.get(mode, 0)


# Window parameters #
resolution = width, height = 1280, 720
window_mode = get_window_mode(0)
fps = 0

# Map parameters #
block_size = 50

# Player parameters #
player_speed = block_size / 1000
rotation_speed = math.pi / 1000
draw_distance = 75
