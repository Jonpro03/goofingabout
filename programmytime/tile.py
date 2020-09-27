class Tile:
    solid_chars = ['=', '|', 'o', 'x']

    def __init__(self, character, loc_in_room):
        self.character = character
        self.solid = False
        self.loc_in_room = loc_in_room

        if character in Tile.solid_chars:
            self.solid = True
