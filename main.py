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
laser_surf = pygame.image.load('./graphics/laser.png').convert_alpha()
laser_rect = laser_surf.get_rect(center = (-100, -100))

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
        # if event.type == pygame.MOUSEMOTION:
        #     ship_rect = ship_surf.get_rect(center= event.pos)
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     laser_rect = laser_surf.get_rect(center = (event.pos))
            

    # Framerate limit
    clock.tick(120)

    # Mouse input
    ship_rect = ship_surf.get_rect(center = pygame.mouse.get_pos())
    laser_rect = laser_surf.get_rect(center = pygame.mouse.get_pressed(event.pos))
    # Updates
    display_surface.fill((0,0,0))
    display_surface.blit(bg_surf,(0,0))
    display_surface.blit(ship_surf,(ship_rect))
    display_surface.blit(text_surf, (text_rect))
    display_surface.blit(laser_surf, (laser_rect))
   
    # Update display surface
    pygame.display.update()