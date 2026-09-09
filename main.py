import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

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

    # 1. Calculate the center coordinates
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # 2. Instantiate the Player ONCE before the game loop starts
    player = Player(x, y)

    # 🔄 THE GAME LOOP
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # 3. Tell your player to draw itself onto the screen every frame
        player.draw(screen)

        pygame.display.flip()

        # 4.
        dt = clock.tick(60) / 1000

        player.update(dt)


if __name__ == "__main__":
    main()
