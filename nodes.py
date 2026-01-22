class Node:
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def tuple(self):
        return (self.x, self.y)
