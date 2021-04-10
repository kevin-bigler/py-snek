import pygame

black = (0, 0, 0)


def create_rect_with_border(width, height, fill_color, border_width=1, border_color=black):
    "Create a rect surface with a border"
    surface = pygame.Surface((width, height))
    surface.fill(fill_color)

    rect = pygame.Rect((0, 0), (width, height))
    pygame.draw.rect(surface, border_color, rect, border_width)

    return surface


def draw_rect_test(surface):
    width, height = 20, 40
    box = create_rect_with_border(width, height, pygame.Color('red'))
    surface.blit(box, (5, 5))
    surface.blit(box, (50, 50))
