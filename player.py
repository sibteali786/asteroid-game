from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH
import pygame


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0,1).rotate(self.rotation) # direction showing which way nose ( trinagle ) points
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5 # direction and distance combined, 1.5 makes sure triangle is not ISOsceles triangle
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]
    
    def draw(self, screen: pygame.Surface ):
        color = "white"
        points = self.triangle()
        width = LINE_WIDTH
        pygame.draw.polygon(screen,color, points, width)
