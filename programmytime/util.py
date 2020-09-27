class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x} y:{self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(f"{self.x}{self.y}")