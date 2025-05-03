# this allows us to use code from
# the open-source pygame library
# throughout this file

# source venv/bin/activate
import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 # delta time since last tick
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_x_init = SCREEN_WIDTH / 2
    player_y_init = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(player_x_init, player_y_init)
    asteroid_field = AsteroidField()
    
    # =============================== Game loop start ========================================
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        
        # see if player collided with asteroid, end game if so
        for asteroid in asteroids:
            if asteroid.collision_Check(player):
                print("Game over!")
                sys.exit()
        
        # see if shot colllided with asteroid, split asteroid and remove shot if so        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_Check(shot):
                    asteroid.split()
                    shot.kill()
        
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000 # 60 fps
    # =============================== Game loop end ========================================
    
    
if __name__ == "__main__":
    main()