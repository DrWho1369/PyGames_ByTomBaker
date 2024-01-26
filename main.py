import pygame, sys
from random import randint, uniform

def laser_update(laser_list, speed = 300):
    for rect in laser_list:
        rect.y -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect)

def display_score():
    score_text = f"Score: {pygame.time.get_ticks() // 1000}"
    text_surf = font.render(f"{score_text} || Logan's SPACE Game", True, 'White')
    text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT-80))
    display_surface.blit(text_surf, (text_rect))
    pygame.draw.rect(display_surface,(255,255,255),text_rect.inflate(30,30), width=8, border_radius=5,)

def laser_timer(can_shoot, duration = 500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot

def met_update(met_list, speed = 400):
    for meteor_tuple in met_list:
        direction = meteor_tuple[1]
        met_rect = meteor_tuple[0]
        met_rect.center += direction * speed * dt

        # rect.y += speed * dt
        if met_rect.top > WINDOW_HEIGHT:
            met_list.remove(meteor_tuple)
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
laser_list = []

# Laser Timer
can_shoot = True
shoot_time = None

# Text Import
font = pygame.font.Font('./graphics/subatomic.ttf', 50)

# Meteor Timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

# Meteor Import
met_surf = pygame.image.load('./graphics/meteor.png').convert_alpha()
met_list = []



while True: 
    # Event Loop
    for event in pygame.event.get():
        #Offer user exit option
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:

            # Laser
            laser_rect = laser_surf.get_rect(midbottom = (ship_rect.midtop))
            laser_list.append(laser_rect)

            # Timer Logic
            can_shoot = False
            shoot_time = pygame.time.get_ticks()

        if event.type == meteor_timer:

            # Random Position
            x_pos = randint(-100, WINDOW_WIDTH + 100)
            y_pos = randint(-100, -50)

            # Creating Rect
            met_rect = met_surf.get_rect(center = (x_pos, y_pos))

            # Create a random direction
            direction = pygame.math.Vector2(uniform(-0.5, 0.5),1)
            
            met_list.append((met_rect, direction))
    # Framerate limit
    dt = clock.tick(120) / 1000

    # Mouse input
    ship_rect.center = pygame.mouse.get_pos()
    
    # Updates
    laser_update(laser_list)
    met_update(met_list)
    can_shoot = laser_timer(can_shoot, 500)

    # Meteor-Ship Collisions
    for meteor_tuple in met_list:
        met_rect = meteor_tuple[0]
        if ship_rect.colliderect(met_rect):
            pygame.quit()
            sys.exit()
    
    # Laser-Meteor Collisions
    
    for laser_rect in laser_list:
        for meteor_tuple in met_list:
            if laser_rect.colliderect(meteor_tuple[0]):
                laser_list.remove(rect)
                met_list.remove(meteor_tuple)
    # Drawing
    display_surface.fill((0,0,0))
    display_surface.blit(bg_surf,(0,0))
    
    display_score()
    
    for rect in laser_list:
        display_surface.blit(laser_surf, (rect))

    display_surface.blit(ship_surf,(ship_rect))

    for meteor_tuple in met_list:
        display_surface.blit(met_surf, (meteor_tuple[0]))
    # Draw Final Frame for User
    pygame.display.update()