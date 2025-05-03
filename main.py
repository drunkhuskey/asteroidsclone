# this allows us to use code from
# the open-source pygame library
# throughout this file

# source venv/bin/activate
import pygame
from constants import *
from player import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

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
    Player.containers = (updatable, drawable)
    player = Player(player_x_init, player_y_init)
    
    # =============================== Game loop start ========================================
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000 # 60 fps
    
    
    
if __name__ == "__main__":
    main()