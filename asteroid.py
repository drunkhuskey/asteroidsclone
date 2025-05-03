import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        angle_one = self.velocity.rotate(angle)
        angle_two = self.velocity.rotate(-angle)
        radius_new = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position[0], self.position[1], radius_new)
        asteroid_two = Asteroid(self.position[0], self.position[1], radius_new)
        asteroid_one.velocity = angle_one * 1.2
        asteroid_two.velocity = angle_two * 1.2
              
    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt