import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Meteor shooter')
clock = pygame.time.Clock()

# importing images 
ship_surf = pygame.image.load('../graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2))
bg_surf = pygame.image.load('../graphics/background.png').convert()

# import text 
font = pygame.font.Font('../graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, (255,255,255))
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))

while True: # run forever -> keeps our game running

	# 1. input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		# if event.type == pygame.MOUSEMOTION:
		# 	# exercise 
		# 	# use the mouse position to control the spaceship
			ship_rect.center = event.pos

		# if event.type == pygame.MOUSEBUTTONDOWN:
		# 	print(event.pos)

	# framerate limit
	clock.tick(120)

	# mouse input 
	# print(pygame.mouse.get_pos())
	# print(pygame.mouse.get_pressed())
	
	# exercise
	# place the ship on the mouse position while using the methods
	ship_rect.center = pygame.mouse.get_pos()

	# 2. updates 
	display_surface.fill((0, 0, 0)) 
	display_surface.blit(bg_surf,(0,0))
	display_surface.blit(ship_surf,ship_rect)
	display_surface.blit(text_surf,text_rect)


	# 3. show the frame to the player / update the display surface
	pygame.display.update()