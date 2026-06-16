import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def draw(self, screen: pygame.Surface):
        color = "white"
        radius = self.radius
        width = LINE_WIDTH
        center = self.position
        pygame.draw.circle(screen, color, center, radius, width)
