import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random 


class Asteroids(CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
	
	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			angle = random.uniform(20, 50)
			a_1_vec = self.velocity.rotate(angle) * 1.2
			a_2_vec = self.velocity.rotate(-angle) * 1.2
			old_rad = self.radius
			rad = old_rad - ASTEROID_MIN_RADIUS
			asteroid_1 = Asteroids(self.position[0], self.position[1], rad)
			asteroid_1.velocity = a_1_vec
			asteroid_2 = Asteroids(self.position[0], self.position[1], rad)
			asteroid_2.velocity = a_2_vec
			
