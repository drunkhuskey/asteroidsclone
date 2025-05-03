# this allows us to use code from
# the open-source pygame library
# throughout this file

# source venv/bin/activate
import pygame
from constants import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 # delta time since last tick
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # =============================== Game loop start ========================================
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000 # 60 fps
    
    
    
if __name__ == "__main__":
    main()