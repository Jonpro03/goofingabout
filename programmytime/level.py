class Level:

    def __init__(self, level_num, width, height):
        self.level_num = level_num
        self.level_file = f"level{self.level_num}.txt"

        self.width = width
        self.height = height
        self.area = height*width

        self.tiles = []

        # for y in range(self.height):
        #     row = []
        #     for x in range(self.width):
        #         row.append(y)
        #     self.tiles.append(row)


    def load_level(self):
        with open(self.level_file, "r") as lvl:
            level_lines = lvl.readlines()
        for y in range(self.height):
            line = level_lines[y]
            row = []
            for x in range(self.width):
                row.append(line[x])
            self.tiles.append(row)



    def draw_screen(self, player_loc_x, player_loc_y):
        for y in range(self.height):
            for x in range(self.width):
                if player_loc_x == x and player_loc_y == y:
                    print("p", end='')
                else:
                    print(self.tiles[y][x], end='')
            print("")
