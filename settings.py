import math
import pygame as pg


def get_window_mode(mode=0):
    modes = {
        0: pg.SHOWN,
        1: pg.NOFRAME,
        2: pg.FULLSCREEN
    }

    return modes.get(mode)


# Window parameters #
resolution = width, height = 1280, 720
window_mode = get_window_mode(0)
fps = 0

# Map parameters #
block_size = 1

# Player parameters #
player_speed = block_size / 300
rotation_speed = math.pi / 1500
draw_distance = 50

scale_2d = 20

# Ray caster parameters #
fov = math.pi / 3
num_rays = width
max_depth = draw_distance
delta_angle = fov / num_rays
screen_distance = (width // 2) / (math.tan(fov / 2))
scale = width // num_rays

# Debug parameter #
set_3d = 1
show_raycaster = 1
