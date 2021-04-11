import pygame, sys

pygame.init()
pygame.font.init()

from rect_with_border import create_rect_with_border
from grid import Grid
from snek import Snek
from food import Food


tile_width, tile_height = (20, 20)

board = Grid(15, 15)
food = Food(board.size)
snek = Snek((4, 2), board.size)

board_width, board_height = board.width * tile_width, board.height * tile_height
board_color = pygame.Color('lightslategray')
board_border_color = pygame.Color('black')
board_border_width = 2

window_title = 'py sneky snek'
window_bg_color = pygame.Color('lightgray')
window_width, window_height = board_width * 2, board_height

MOVE_SNEK = pygame.USEREVENT
pygame.time.set_timer(MOVE_SNEK, 300)
paused = False

def draw_board(grid: Grid, surface: pygame.Surface):
    """Draw board where snek is."""
    # for val, (x, y) in grid:
    #     color = pygame.Color('pink')
    #     tile = create_rect_with_border(tile_width, tile_height, fill_color=color, border_width=0)
    #     surface.blit(tile, (x * tile_width, y * tile_height))
    border = pygame.rect.Rect(0, 0, board_width, board_height)
    pygame.draw.rect(surface, board_border_color, border, board_border_width)


def draw_food(food: Food, surface: pygame.Surface):
    tile = create_rect_with_border(tile_width, tile_height, fill_color=pygame.Color('orange'), border_color=pygame.Color('white'))
    surface.blit(tile, (food.position.x * tile_width, food.position.y * tile_height))


def draw_snek(snek: Snek, surface: pygame.Surface):
    for block in snek:
        if block == snek.body[0]:
            color = pygame.Color('darkgreen')#'limegreen')
        else:
            color = pygame.Color('green')
        
        tile = create_rect_with_border(tile_width, tile_height, fill_color=color, border_color=pygame.Color('black'))
        surface.blit(tile, (block.x * tile_width, block.y * tile_height))
    

def draw_stats(surface):
    margin = 10
    draw_text(f'Score: {len(snek.body) - 2}', surface, (margin + 0, margin + 0))


def draw_text(text, surface, position):
    font = pygame.font.SysFont('Arial', 20)
    text_render = font.render(text, True, pygame.Color('black'))
    
    text_rect = text_render.get_rect(topleft = position)
    surface.blit(text_render, text_rect)


screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)
clock = pygame.time.Clock()


def update_state():
    snek.check_eat(food)
    snek.check_dead()


def draw():
    screen.fill(window_bg_color)

    board_surface = pygame.Surface((board_width, board_height))
    board_surface.fill(board_color)
    draw_board(board, board_surface)
    draw_food(food, board_surface)
    draw_snek(snek, board_surface)
    draw_stats(screen)
    board_rect = board_surface.get_rect(center = (window_width / 2, window_height / 2))
    screen.blit(board_surface, board_rect)

    pygame.display.update()


while True:
    # Handle input
    time_to_move = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # timer moving snek
        if event.type == MOVE_SNEK:
            if not paused:
                snek.move()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snek.turn_up()
            if event.key == pygame.K_DOWN:
                snek.turn_down()
            if event.key == pygame.K_LEFT:
                snek.turn_left()
            if event.key == pygame.K_RIGHT:
                snek.turn_right()
            
            # manual moving with space
            if event.key == pygame.K_SPACE:
                paused = not paused
            
            if event.key == pygame.K_ESCAPE:
                # reset board # TODO
                pygame.quit()
                sys.exit()

    # if time_to_move:
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_SPACE]:
    #         snek.move()

    update_state()
    draw()
    clock.tick(60)