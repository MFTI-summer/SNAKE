import pygame

display = pygame.display.set_mode((800, 600))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
