import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    # 💥 THE FINAL BULLETPROOF SPLITTING METHOD
    def split(self):
        # 1. Kill the current big asteroid first
        self.kill()

        # 2. If it is already a small pebble, stop right here!
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # 3. Log the split event for Boot.dev
        log_event("asteroid_split")

        # 4. Generate the random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # 5. Rotate the vectors to get the two new flying paths
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)

        # 6. Compute the new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # 7. Grab the precise current coordinate values
        pos_x = self.position.x
        pos_y = self.position.y

        # 8. Spawn the two new smaller child fragments
        asteroid1 = Asteroid(pos_x, pos_y, new_radius)
        asteroid2 = Asteroid(pos_x, pos_y, new_radius)

        # 🚨 THE SECRET SAUCE: Force them to copy the parent's container tracking groups!
        # This overrides any hidden bugs and forces them onto the screen.
        if hasattr(self, "containers"):
            asteroid1.add(self.containers)
            asteroid2.add(self.containers)

        # 9. Scale up their speed by 1.2 so they zip away
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2
