import pygame, sys,

# Game Init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("LOGAN'S METEOR SHOOTER")
clock = pygame.time.Clock()

# Ship Import
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

# Background Import
bg_surf = pygame.image.load('./graphics/background.png').convert()

# Laser Import
laser_surf = pygame.image.load('./graphics/laser.png').convert_alpha()
laser_rect = laser_surf.get_rect(center = (ship_rect.midtop))

# Text Import
font = pygame.font.Font('./graphics/subatomic.ttf', 50)
text_surf = font.render("Logan's SPACE Game", True, 'White')
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT-80))

# Meteor Import
met_surf = pygame.image.load('./graphics/meteor.png').convert_alpha()
met_rect = met_surf.get_rect(center = (WINDOW_HEIGHT/2, WINDOW_WIDTH/2))
# Drawing


while True: 
    # Event Loop
    for event in pygame.event.get():
        #Offer user exit option
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Framerate limit
    dt = clock.tick(120) / 1000

    # Mouse input
    ship_rect.center = pygame.mouse.get_pos()
    
    # Updates
    laser_rect.y -= round(200 * dt)

    # Drawing
    display_surface.fill((0,0,0))
    display_surface.blit(bg_surf,(0,0))
    
    display_surface.blit(text_surf, (text_rect))
    pygame.draw.rect(display_surface,(255,255,255),text_rect.inflate(30,30), width=8, border_radius=5,)
    
    display_surface.blit(laser_surf, (laser_rect))
    display_surface.blit(ship_surf,(ship_rect))

    display_surface.blit(met_surf, (met_rect))
    # Draw Final Frame for User
    pygame.display.update()