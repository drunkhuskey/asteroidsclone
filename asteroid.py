import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt