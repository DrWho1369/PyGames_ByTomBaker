import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Meteor shooter')

# create a surface 
test_surf = pygame.Surface((200,100))
# we need to attach the surface to the display surface 
# both the display surface and the surface are black

while True: # run forever -> keeps our game running

	# 1. input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# 2. updates 
	display_surface.fill((15, 140, 122)) 
	test_surf.fill((186, 120, 39))

	# place a surface
	# Exercise: Place the test surface so that the the is on the right side of the display surface
	display_surface.blit(test_surf,(WINDOW_WIDTH - test_surf.get_width(),100))

	# 3. show the frame to the player / update the display surface
	pygame.display.update()