import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("LOGAN'S SPACE GAME")

# Suface
test_surf = pygame.Surface((400,100))



while True: 
    # Input -> events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Updates
    display_surface.fill((15,140,122))
    test_surf.fill('darkgoldenrod3')
    display_surface.blit(test_surf, (50,50))
    # Update display surface
    pygame.display.update()