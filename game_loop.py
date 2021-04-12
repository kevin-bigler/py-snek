import pygame

class GameLoop:
    def __init__(self, skip_init = False):
        """
        Creates GameLoop instance, purely focused on timing and exiting on clicking 'X' and nothing else.
        Args
            skip_init: Optional, default false. Whether to skip pygame.init() invocation upon creation. Default is to run init
        """
        pygame.init() # this should probably just be called in whatever main file the game starts in...
        self.clock = pygame.time.Clock()

    def run(self, tick):
        """
        Starts GameLoop, invoking `tick` function on each iteration, like `tick(dt)`, where `dt` is delta time.
        """
        dt = 0

        while True:
            # Handle exit input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            tick(dt)

            # pygame.display.update() # should this be done in tick-implementation, or here?
            dt = self.clock.tick(60)

window_title = 'game loop test'
window_bg_color = pygame.Color('lightgray')
window_width, window_height = 1280, 720
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)

import random
def game_tick(dt):
    print(f'hello {random.randrange(10)}')


    pygame.display.update()

game_loop = GameLoop()
game_loop.run(game_tick)