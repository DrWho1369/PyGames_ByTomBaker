import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("LOGAN'S METEOR SHOOTER")
clock = pygame.time.Clock()

# Images
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

bg_surf = pygame.image.load('./graphics/background.png').convert()

# Text
font = pygame.font.Font('./graphics/subatomic.ttf', 50)
text_surf = font.render("Logan's SPACE Game", True, 'White')
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT-80))

while True: 
    # Input -> events
    for event in pygame.event.get():
        #Offer user exit option
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Framerate limit
    clock.tick(120)

    # Updates
    display_surface.fill((0,0,0))
    display_surface.blit(bg_surf,(0,0))
    if ship_rect.top > 0:
        ship_rect.y -= 4
    display_surface.blit(ship_surf,(ship_rect))
    display_surface.blit(text_surf, (text_rect))
    # Update display surface
    pygame.display.update()