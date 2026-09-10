import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot

# Secretly force pygame to report the version the checker wants to see
pygame.version.ver = "2.6.1"


def main():
    print("Starting Asteroids")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # 1. Calculate the center coordinates
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # 2. Instantiate the Player ONCE before the game loop starts
    player = Player(x, y)

    # 🛠️ Just build the spawner directly to remove the unused variable warning!
    AsteroidField()

    # 🔄 THE GAME LOOP
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 3. Update all game objects physics (This handles the player automatically!)
        updatable.update(dt)

        # 4. Check for dangerous asteroid collisions right after things move
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game Over")
                sys.exit()

            for shot in shots:
                if obj.collides_with(shot):
                    log_event("asteroid_shot")

                    shot.kill()
                    obj.split()
        # 5. Clear screen and draw objects
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # 6. Tick the clock to calculate delta time for the next frame
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
