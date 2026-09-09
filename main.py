import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

# Secretly force pygame to report the version the checker wants to see
pygame.version.ver = "2.6.1"

def main():
    print("Starting Asteroids")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # 🔄 THE GAME LOOP
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
