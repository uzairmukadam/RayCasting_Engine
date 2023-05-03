import json

from settings import *


class Map:
    def __init__(self, game):
        self.game = game

        self.map = {}
        self.wall = {}
        self.wall_color = {}
        self.start_block = None

    def load_map(self, map_id):
        with open(map_dir + map_id + ".json", "r") as map_file:
            map_data = json.load(map_file)

            i, j = map_data["map_dimen"]

            for y in range(j):
                for x in range(i):
                    floor = map_data["floor_map"][x][y]
                    wall_height = map_data["wall_map"][x][y]
                    ceiling = map_data["ceiling_map"][x][y]

                    self.map[x, y] = [floor, wall_height, ceiling]

            for wall in map_data["wall_id"]:
                self.wall[wall] = map_data["wall_color"][str(wall)]

            self.start_block = map_data["start_block"]
