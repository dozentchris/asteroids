from pygame import Surface
import pygame
from constants import *
import random

from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")
            randAngle = random.uniform(20,50)
            a2v = self.velocity.rotate(randAngle)
            a1v = self.velocity.rotate(-abs(randAngle))
            self.radius -= ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, self.radius)
            a2 = Asteroid(self.position.x, self.position.y, self.radius)
            a1.velocity = a1v * 1.2
            a2.velocity = a2v * 1.2

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", (self.position), self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)