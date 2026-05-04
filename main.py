import pygame
import math
import sys
from weather import fetch_weather

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Weather Visualiser")
clock = pygame.time.Clock()
font_big = pygame.font.SysFont("monospace", 24)

def draw_rain(weather):
    screen.fill((55, 71, 79))

    # Dark clouds
    pygame.draw.ellipse(screen, (84, 110, 122), (0, 20, 220, 80))
    pygame.draw.ellipse(screen, (69, 90, 100), (80, 10, 180, 80))
    pygame.draw.ellipse(screen, (84, 110, 122), (200, 25, 240, 80))
    pygame.draw.ellipse(screen, (69, 90, 100), (320, 15, 200, 80))
    pygame.draw.ellipse(screen, (84, 110, 122), (480, 20, 220, 80))
    pygame.draw.ellipse(screen, (69, 90, 100), (620, 10, 200, 80))
    # House
    pygame.draw.polygon(screen, (204, 62, 43), [(385, 350), (665, 350), (525, 260)])
    pygame.draw.rect(screen, (204, 62, 43), (560, 250, 30, 80))
    pygame.draw.rect(screen, (196, 157, 120), (400, 350, 250, 150))
    pygame.draw.rect(screen, (204, 62, 43), (493, 400, 60, 100))

    # Left window
    pygame.draw.rect(screen, (224, 224, 224), (417, 370, 60, 60))
    pygame.draw.rect(screen, (130, 234, 245), (422, 375, 50, 50))
    pygame.draw.line(screen, (224, 224, 224), (447, 375), (447, 425), 3)
    pygame.draw.line(screen, (224, 224, 224), (422, 400), (472, 400), 3)

    # Right window
    pygame.draw.rect(screen, (224, 224, 224), (570, 370, 60, 60))
    pygame.draw.rect(screen, (130, 234, 245), (575, 375, 50, 50))
    pygame.draw.line(screen, (224, 224, 224), (600, 375), (600, 425), 3)
    pygame.draw.line(screen, (224, 224, 224), (575, 400), (625, 400), 3)
    
    # Tree
    pygame.draw.rect(screen, (138, 51, 36), (50, 350, 35, 200))
    pygame.draw.polygon(screen, (0, 128, 0), [(70, 240), (18, 370), (117, 370)])
    pygame.draw.polygon(screen, (0, 128, 0), [(70, 180), (30, 310), (105, 310)])
    pygame.draw.polygon(screen, (0, 128, 0), [(70, 270), (6, 430), (128, 430)])

    # Rain drops
    t = int(pygame.time.get_ticks() / 50)
    for i in range(100):
        x = (i * 137 + t * 3) % WIDTH
        y = (i * 97 + t * 8) % (HEIGHT - 80)
        pygame.draw.line(screen, (144, 202, 249), (x, y), (x - 3, y + 15), 2)
    # Ground
    pygame.draw.rect(screen, (23, 56, 8), (0, 500, WIDTH, 100))
    # Weather info box
    pygame.draw.rect(screen, (0, 0, 0), (0, 545, WIDTH, 55))
    city_text = font_big.render(
        f"{weather['city']}  {weather['temperature']:.1f}C  {weather['condition']}  Wind: {weather['wind_speed']:.1f} m/s",
        True, (144, 202, 249))
    screen.blit(city_text, (15, 560))


def main():
    print("Fetching weather...")
    weather = fetch_weather("Brisbane")
    if not weather:
        weather = {
            "city": "Brisbane",
            "condition": "Clear",
            "temperature": 25.0,
            "wind_speed": 3.0
        }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        draw_rain(weather)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
