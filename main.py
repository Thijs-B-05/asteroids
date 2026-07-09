import pygame
from logger import (log_state, log_event )
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from circleshape import CircleShape
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0.0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}\nScreen width: 1280\nScreen height: 720")
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots  = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroids.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	player = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT / 2)
	asteroidfield = AsteroidField()
	while True:
		#log game events
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		#update all updatable events
		updatable.update(dt)
		#collission check player asteroid
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				sys.exit()
		#collision check bullet asteroid
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collides_with(shot):
					log_event("asteroid_shot")
					asteroid.split()
		#make up screen
		screen.fill("black")
		#player
		for player__ in drawable:
			player__.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		
if __name__ == "__main__":
    main()
