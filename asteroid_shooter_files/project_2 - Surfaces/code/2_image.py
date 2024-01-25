import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Meteor shooter')

# create a surface 
test_surf = pygame.Surface((400,100))
# we need to attach the surface to the display surface 
# both the display surface and the surface are black

while True: # run forever -> keeps our game running

	# 1. input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# 2. updates 
	display_surface.fill((15, 140, 122)) # https://www.pygame.org/docs/ref/color_list.html
	# exercise: fill the test surface with a gold orangy color
	test_surf.fill((186, 120, 39))
	display_surface.blit(test_surf,(0,0))

	# 3. show the frame to the player / update the display surface
	pygame.display.update()