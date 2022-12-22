import pygame

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, bulletSpeed = 5):
		pass

	def update(self):
		# Move the bullet
		self.rect.x += self.bulletSpeed
