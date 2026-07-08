import pygame
from logger import log_state
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from circleshape import CircleShape
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0.0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}\n Screen width: 1280\n Screen height: 720")
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroids.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	player = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT / 2)
	asteroidfield = AsteroidField()
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for player in drawable:
			player.draw(screen)
		updatable.update(dt)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		
if __name__ == "__main__":
    main()
