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
food = Food((10, 5))
snek = Snek((4, 2))

def draw_board(grid: Grid, surface: pygame.Surface):
    """Draw board where snek is."""
    for val, (x, y) in grid:
        color = pygame.Color('pink')
        tile = create_rect_with_border(tile_width, tile_height, fill_color=color)
        surface.blit(tile, (x * tile_width, y * tile_height))


def draw_food(food: Food, surface: pygame.Surface):
    tile = create_rect_with_border(tile_width, tile_height, fill_color=pygame.Color('orange'))
    surface.blit(tile, (food.position.x * tile_width, food.position.y * tile_height))


def draw_snek(snek: Snek, surface: pygame.Surface):
    for block in snek:
        tile = create_rect_with_border(tile_width, tile_height, fill_color=pygame.Color('green'))
        surface.blit(tile, (block.x * tile_width, block.y * tile_height))


screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)
clock = pygame.time.Clock()

def draw():
    screen.fill(window_bg_color)
    draw_board(board, screen)
    draw_food(food, screen)
    draw_snek(snek, screen)
    pygame.display.update()

while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snek.turn_up()
            if event.key == pygame.K_DOWN:
                snek.turn_down()
            if event.key == pygame.K_LEFT:
                snek.turn_left()
            if event.key == pygame.K_RIGHT:
                snek.turn_right()
            
            if event.key == pygame.K_SPACE:
                snek.move()

    draw()
    clock.tick(60)