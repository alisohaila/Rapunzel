import pygame, sys
from pygame.locals import QUIT
from rapunzel import Rapunzel
from bullet import Bullet

BLUE = (148, 204, 242)
GROUNDCOLOR = (100, 255, 0)

GROUND = 350
WIDTH = 400
HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rapunzel Battle')

# Create the sprite and scale the image to 10% of the original size
player = Rapunzel("rap.jpg", .3,.3)
player.flip(True, False)


clock = pygame.time.Clock()

while True:
	clock.tick(200)
	screen.fill(BLUE)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		# Fire the bullet... currently there is no code in fire()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.fire()

	# Make sure to call "update()" to move the player
	player.update()
	
	screen.blit(player.image, player.rect)

	# Code to go through the list of bullets and update their positions
	for b in player.bullets:
		b.update()
		screen.blit(b.image, b.rect)


	# Draw ground
	pygame.draw.rect(screen,GROUNDCOLOR, pygame.Rect(0,  GROUND, WIDTH,HEIGHT - GROUND))
	
	
	pygame.display.update()
