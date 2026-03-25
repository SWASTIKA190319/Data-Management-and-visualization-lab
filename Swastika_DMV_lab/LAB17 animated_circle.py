import pygame
import sys

# ---- USER INPUT ----
try:
    speed = float(input("Enter circle speed (e.g., 2 to 10): "))
    radius = int(input("Enter circle size (radius, e.g., 10 to 100): "))
    fps = int(input("Enter frame rate (e.g., 30 to 120): "))
except:
    print("Invalid input! Using default values.")
    speed, radius, fps = 5, 30, 60

# Initialize pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle")

clock = pygame.time.Clock()

# Initial position
x, y = width // 2, height // 2
speed_x, speed_y = speed, speed

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)

# ---- MAIN LOOP ----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move circle
    x += speed_x
    y += speed_y

    # Bounce off walls
    if x - radius <= 0 or x + radius >= width:
        speed_x *= -1
    if y - radius <= 0 or y + radius >= height:
        speed_y *= -1

    # Draw
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (int(x), int(y)), radius)

    pygame.display.flip()
    clock.tick(fps)