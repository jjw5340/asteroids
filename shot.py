import pygame

from constants import LINE_WIDTH, SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            SHOT_RADIUS,
            LINE_WIDTH
        )

    def update(self, dt: float):
        self.position += self.velocity * dt
