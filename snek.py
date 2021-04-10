from pygame.math import Vector2


class Snek:
    def __init__(self, start_pos = (0, 0)):
        self.direction = Vector2(0, 0)
        self.body = [Vector2(start_pos)]
    
    def turn_up(self):
        self.direction = Vector2(0, -1)
    
    def turn_down(self):
        self.direction = Vector2(0, 1)
    
    def turn_left(self):
        self.direction = Vector2(-1, 0)
    
    def turn_right(self):
        self.direction = Vector2(1, 0)

    def move(self):
        new_block = self.body[0] + self.direction
        body_copy = self.body[:-1]
        body_copy.insert(0, new_block)
        self.body = body_copy
    
    def __iter__(self):
        for block in self.body:
            yield block

