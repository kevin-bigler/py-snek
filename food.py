from pygame.math import Vector2
import random


class Food:
    def __init__(self, pos_range = (1, 1)):
        self.position = Vector2(0, 0)
        self.pos_range = Vector2(pos_range)
        self.randomize()
    
    def randomize(self):
        rand_x = random.randrange(self.pos_range.x)
        rand_y = random.randrange(self.pos_range.y)
        self.position = Vector2(rand_x, rand_y)
    
