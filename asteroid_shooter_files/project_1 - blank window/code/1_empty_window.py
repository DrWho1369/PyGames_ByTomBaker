import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# exercise: research 
# website: https://www.pygame.org/docs/ref/display.html
# use a method to change the title of the window
pygame.display.set_caption('Meteor shooter')

while True: # run forever -> keeps our game running

	# 1. input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# 2. updates 
	# nothing yet :) 

	# 3. show the frame to the player / update the display surface
	pygame.display.update()