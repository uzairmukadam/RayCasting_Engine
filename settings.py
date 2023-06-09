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
map_dir = "data/map/"
assets_dir = "data/assets/textures/"

# Player parameters #
player_speed = block_size / 400
vertical_speed = height / 100
rotation_speed = math.pi / 2000
draw_distance = 20
outer_radius = block_size / 4

scale_2d = 10

# Ray caster parameters #
fov = math.pi / 3
num_rays = width
max_depth = draw_distance
delta_angle = fov / num_rays
screen_distance = (width // 2) / (math.tan(fov / 2))
scale = width // num_rays

# Texture parameters #
texture_size = 64

# Debug parameter #
set_3d = 1
show_raycaster = 0
