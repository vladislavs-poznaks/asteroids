import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)

        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2 = Asteroid(self.position, self.position.y, radius)

        asteroid1.velocity = self.velocity.rotate(-split_angle) * 1.2
        asteroid2.velocity = self.velocity.rotate(split_angle) * 1.2

