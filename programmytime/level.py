# class Level:

#     def __init__(self, level_num, width, height):
#         self.level_num = level_num
#         self.level_file = f"level{self.level_num}.txt"

#         self.width = width
#         self.height = height
#         self.area = height*width

#         self.tiles = []

#         # for y in range(self.height):
#         #     row = []
#         #     for x in range(self.width):
#         #         row.append(y)
#         #     self.tiles.append(row)


#     def load_level(self):
#         with open(self.level_file, "r") as lvl:
#             level_lines = lvl.readlines()
#         for y in range(self.height):
#             line = level_lines[y]
#             row = []
#             for x in range(self.width):
#                 row.append(line[x])
#             self.tiles.append(row)



#     def draw_screen(self, player_loc_x, player_loc_y):
#         for y in range(self.height):
#             for x in range(self.width):
#                 if player_loc_x == x and player_loc_y == y:
#                     print("p", end='')
#                 else:
#                     print(self.tiles[y][x], end='')
#             print("")

import os
from room import Room
from tile import Tile
from util import Vector2

class Level:
    def __init__(self, name):
        self.name = name
        self.rooms = []

        file_names = os.listdir(self.name)
        print(file_names)
        for file_name in file_names:
            level_loc_x = int(file_name[4])
            level_loc_y = int(file_name[6])
            level_loc = Vector2(level_loc_x, level_loc_y)
            
            file_path = os.path.join(self.name, file_name)
            with open(file_path, 'r') as file_obj:
                lines = file_obj.readlines()
                width = len(lines[0])
                height = len(lines)
                print(f"Loading level: {file_name}. Height: {height}. Width: {width}")

                tiles = {}
                for y in range(height):
                    for x in range(width):
                        loc_in_room = Vector2(x,y)
                        tile = Tile(lines[y-1][x-1], loc_in_room)
                        tiles[loc_in_room] = tile

            room = Room(level_loc, width, height, tiles)
            self.rooms.append(room)


