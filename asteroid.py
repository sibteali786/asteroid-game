from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        color = "white"
        radius = self.radius
        width = LINE_WIDTH
        center = self.position
        pygame.draw.circle(screen, color, center, radius, width)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            first_vector = self.velocity.rotate(random_angle)
            second_vector = self.velocity.rotate(-random_angle)
            first_radius = self.radius - ASTEROID_MIN_RADIUS
            second_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, first_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, second_radius)
            asteroid_1.velocity = first_vector * 1.2
            asteroid_2.velocity = second_vector * 1.2
