import pygame, sys

pygame.init()

from rect_with_border import create_rect_with_border
from grid import Grid
from snek import Snek
from food import Food


tile_width, tile_height = (20, 20)

board = Grid(20, 20)
food = Food(board.size)
food.position = pygame.math.Vector2(19, 19)
snek = Snek((4, 2), board.size)

window_title = 'py sneky snek'
window_bg_color = pygame.Color('white')
window_width, window_height = board.width * tile_width, board.height * tile_height

MOVE_SNEK = pygame.USEREVENT
pygame.time.set_timer(MOVE_SNEK, 300)

def draw_board(grid: Grid, surface: pygame.Surface):
    """Draw board where snek is."""
    for val, (x, y) in grid:
        color = pygame.Color('pink')
        tile = create_rect_with_border(tile_width, tile_height, fill_color=color, border_width=0)
        surface.blit(tile, (x * tile_width, y * tile_height))


def draw_food(food: Food, surface: pygame.Surface):
    tile = create_rect_with_border(tile_width, tile_height, fill_color=pygame.Color('orange'))
    surface.blit(tile, (food.position.x * tile_width, food.position.y * tile_height))


def draw_snek(snek: Snek, surface: pygame.Surface):
    for block in snek:
        if block == snek.body[0]:
            color = pygame.Color('limegreen')
        else:
            color = pygame.Color('lightgreen')
        
        tile = create_rect_with_border(tile_width, tile_height, fill_color=color)
        surface.blit(tile, (block.x * tile_width, block.y * tile_height))


screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)
clock = pygame.time.Clock()


def update_state():
    snek.check_eat(food)
    snek.check_dead()


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
            
            ## manual moving with space
            if event.key == pygame.K_SPACE:
                snek.move()
        
        # timer moving snek
        # if event.type == MOVE_SNEK:
        #     snek.move()

    update_state()
    draw()
    clock.tick(60)