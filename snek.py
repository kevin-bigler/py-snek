from pygame.math import Vector2
from food import Food
import random, json


class Snek:
    def __init__(self, start_pos = (0, 0), bounds = (1, 1)):
        self.bounds = Vector2(bounds)
        self.growing = False
        self.reset(start_pos)
    
    def reset(self, pos = None):
        if pos is None:
            pos = Vector2(int(random.randrange(self.bounds.x)), int(random.randrange(self.bounds.y)))
        self.body = [Vector2(pos), Vector2(pos)]
        self.direction = Vector2(0, 0)
    
    def try_turn_to(self, x, y):
        new_dir = Vector2(x, y)
        if self.body[0] + new_dir != self.body[1]:
            self.direction = new_dir

    def turn_up(self):
        self.try_turn_to(0, -1)
    
    def turn_down(self):
        self.try_turn_to(0, 1)
    
    def turn_left(self):
        self.try_turn_to(-1, 0)
    
    def turn_right(self):
        self.try_turn_to(1, 0)

    def move(self):
        new_block = self.body[0] + self.direction

        if self.growing:
            body_copy = self.body[:]
            self.growing = False
        else:
            body_copy = self.body[:-1]
        
        body_copy.insert(0, new_block)
        self.body = body_copy
        print('snek:', self)
    
    def __iter__(self):
        for block in self.body:
            yield block

    def check_eat(self, food: Food):
        if self.body[0] == food.position:
            self.grow()
            while True:
                food.randomize()
                if food.position not in self.body:
                    break

    def grow(self):
        self.growing = True

    def check_dead(self):
        head = self.body[0]
        # self-collision
        if len(self.body) > 2:
            for block in self.body[1:]:
                if head == block:
                    self.die()
        # wall collision
        if head.x < 0 or head.x >= self.bounds.x:
            self.die()
        if head.y < 0 or head.y >= self.bounds.y:
            self.die()
    
    def die(self):
        # self.reset(self.body[0:1])
        self.growing = False
        self.reset()

    def export_json(self):
        """Export body in a JSON-compatible format"""
        body_arr = [[int(block.x), int(block.y)] for block in self.body]
        print('snek body exported to data')
        return {'body': body_arr}
    
    def load_from_json(self, data):
        """Set body values based on JSON-compatible input"""
        self.body = [Vector2(block[0], block[1]) for block in data['body']]
        print('snek body imported from data')
    
    def __repr__(self):
        return json.dumps(self.export_json())
