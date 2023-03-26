import pygame as pg
import sys

from settings import *
from map import *
from player import *
from ray_caster import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(resolution, window_mode)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    # load all the required class #
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.ray_caster = RayCaster(self)

    # check for the event #
    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    # update as per the event #
    def update(self):
        self.player.update()
        self.ray_caster.update()
        pg.display.flip()

        self.delta_time = self.clock.tick(fps)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    # draw as per the update #
    def draw(self):
        self.screen.fill('black')

        if set_3d:
            if show_raycaster:
                self.ray_caster.draw3d()
        else:
            self.map.draw()
            self.player.draw()
            if show_raycaster:
                self.ray_caster.draw()

    # game loop #
    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
