import pygame, sys

from rect_with_border import create_rect_with_border
from grid import Grid
from snek import Snek
from food import Food

window_width, window_height = 400, 200
window_title = 'py sneky snek'
window_bg_color = pygame.Color('white')

tile_width, tile_height = (20, 20)

board = Grid(10, 5)


def draw_board(grid: Grid, surface: pygame.Surface):
    """Draw board where snek is."""
    for val, (x, y) in grid:
        color = pygame.Color('pink')
        print(f'color of val at ({x}, {y}) is {color}')
        tile = create_rect_with_border(tile_width, tile_height, fill_color=color)
        surface.blit(tile, (x * tile_width, y * tile_height))


def draw_snek(snek: Snek):
    pass


def draw_food(food: Food):
    pass


screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)
clock = pygame.time.Clock()

def draw():
    screen.fill(window_bg_color)
    draw_board(board, screen)
    pygame.display.update()

while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw()
    clock.tick(60)