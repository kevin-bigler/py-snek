import pygame

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption('Tetris!')
clock = pygame.time.Clock()

while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # # Visuals
    screen.fill(pygame.Color('white'))
    # tick(self.screen)
    draw_rect_test(screen)

    # # Updating the window
    pygame.display.update()
    clock.tick(60)