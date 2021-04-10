from pygame.math import Vector2
from food import Food


class Snek:
    def __init__(self, start_pos = (0, 0), bounds = (1, 1)):
        self.direction = Vector2(0, 0)
        self.body = [Vector2(start_pos)]
        self.bounds = Vector2(bounds)
        self.growing = False
    
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

        # body_copy = self.body[:] if self.growing else self.body[:-1]
        if self.growing:
            body_copy = self.body[:]
            self.growing = False
        else:
            body_copy = self.body[:-1]
        
        body_copy.insert(0, new_block)
        self.body = body_copy
    
    def __iter__(self):
        for block in self.body:
            yield block

    def check_eat(self, food: Food):
        if self.body[0] == food.position:
            self.grow()
            food.randomize()

    def grow(self):
        self.growing = True

    def check_dead(self):
        head = self.body[0]
        for block in self.body[1:]:
            if head == block:
                self.die()
    
    def die(self):
        self.body = self.body[0:1]
        self.direction = Vector2(0, 0)