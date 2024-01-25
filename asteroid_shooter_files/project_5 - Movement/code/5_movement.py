import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Meteor shooter')
clock = pygame.time.Clock()

# importing images 
ship_surf = pygame.image.load('../graphics/ship.png').convert_alpha()
ship_y_pos = 500
bg_surf = pygame.image.load('../graphics/background.png').convert()

# import text 
font = pygame.font.Font('../graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, (255,255,255))

while True: # run forever -> keeps our game running

	# 1. input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# framerate limit
	clock.tick(120)

	# 2. updates 
	display_surface.fill((0, 0, 0)) 
	display_surface.blit(bg_surf,(0,0))
	ship_y_pos -= 4
	display_surface.blit(ship_surf,(300,ship_y_pos))
	display_surface.blit(text_surf,(500,200))


	# 3. show the frame to the player / update the display surface
	pygame.display.update()