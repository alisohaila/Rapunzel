import pygame
from bullet import Bullet

# Defining values
JUMP_SPEED = [0, -4]
SPEEDX = [1, 0]
MAX_JUMP = 100
RIGHT_EDGE = 400
GROUND = 350

# making a new class
class Rapunzel:
	def __init__(self, filename="rap.jpg", scaleX=5, scaleY=5, x=0, y=0, speed=[1, 0], gravity=[0, 2], ground = 350):
		
		rapunzel = pygame.image.load(filename)
		
		w = rapunzel.get_width()*scaleX
		h = rapunzel.get_height()*scaleY

		self.image = pygame.transform.scale(rapunzel, (w, h))
		self.rect = self.image.get_rect()
		
		self.x = x
		self.y = y
		
		self.speed = speed
		self.gravity = gravity
		self.ground = ground
		self.landed = False
		self.jump = 0
		self.facingLeft = True

		# An empty list that will keep track of bullets fired from this character
		self.bullets = []

	def flip(self, x=True, y=True):
		self.image = pygame.transform.flip(self.image, x, y)

		
	def move(self, speed):
		self.rect = self.rect.move(speed)
	

	def update(self):	
		#check for keys pressed		
		keys_pressed = pygame.key.get_pressed()

		# Code for UP key does NOT work...
        # if keys_pressed[pygame.K_UP] and self.landed:
        #     self.jump = MAX_JUMP
             
        # if self.jump > 0:
        #     self.jump -= 1
        #     self.landed = False
        #     self.move(JUMP_SPEED)

		if keys_pressed[pygame.K_RIGHT]:
			self.move(SPEEDX)
			if self.facingLeft:
				self.flip(True, False)
				self.facingLeft = False

		# You can keep the character faced in one direction and DO NOT have to flip direction...
		if keys_pressed[pygame.K_LEFT]:
			self.move([-SPEEDX[0], -SPEEDX[1]])
			if not self.facingLeft:
				self.flip(True, False)
				self.facingLeft = True

		# "Apply gravity" and bring the code down 
		if self.rect.bottom < GROUND:
			# Apply gravity		
			self.move(self.gravity)
			
		# Land on the ground
		if self.rect.bottom >= self.ground:
			self.rect.bottom = self.ground
			self.landed = True

		# Code for for checking bullets not provided...

	# Code for creating and adding a new bullet not provided
	def fire(self):
		pass
