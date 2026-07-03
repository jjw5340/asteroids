import random

import pygame

from constants import (
    LINE_WIDTH,
    ASTEROID_MIN_RADIUS,
    SPLIT_ANGLE_MIN,
    SPLIT_ANGLE_MAX,
    SPLIT_ASTEROID_VELOCITY_COEF
)
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        split_angle = random.uniform(SPLIT_ANGLE_MIN, SPLIT_ANGLE_MAX)

        split_asteroid_one_vel = self.velocity.rotate(split_angle)
        split_asteroid_two_vel = self.velocity.rotate(-split_angle)

        split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid_one = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
        split_asteroid_two = Asteroid(self.position.x, self.position.y, split_asteroid_radius)

        split_asteroid_one.velocity = SPLIT_ASTEROID_VELOCITY_COEF * split_asteroid_one_vel
        split_asteroid_two.velocity = SPLIT_ASTEROID_VELOCITY_COEF * split_asteroid_two_vel
