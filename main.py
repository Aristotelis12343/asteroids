import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    dt = 0

    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2) 
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.check_for_collisions(player):
                print("Game over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)
       
        pygame.display.flip()
        dt= clock.tick(60) / 1000

if __name__=="__main__":
    main()


