import pygame
import sys

pygame.init()

width = 600
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Praktikum PBO - Pygame")

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

index = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                index = (index + 1) % len(colors)


    # pygame.draw.rect(screen, Red, (100, 100, 200, 150))
    # pygame.draw.circle(screen, Green, (400, 300), 50)
    screen.fill(colors[index])
    pygame.display.flip()

pygame.quit()
sys.exit()