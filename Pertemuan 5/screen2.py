import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame. display.set_mode ((WIDTH, HEIGHT) )
pygame.display.set_caption("Game PBO")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

class Player:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

        self.width = 50
        self.height = 58

        self.speed = 2

        self.colored = colors[0]

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += self.speed
    
    def color(self, keys):
        if keys[pygame.K_1]:
            self.colored = colors[1]
        if keys[pygame.K_2]:
            self.colored = colors[2]
        if keys[pygame.K_3]:
            self.colored = colors[0]

    def size(self, keys):
        if keys[pygame.K_p] and self.width < 400:
            self.width = self.width + 1
            self.height = self.height + 1
        if keys[pygame.K_o] and self.width > 50:
            self.width = self.width - 1
            self.height = self.height - 1

    def draw(self, surface):
        pygame.draw.rect(surface, self.colored, (self.x, self.y, self.width, self.height))

player = Player(375,275)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    press = pygame.key.get_pressed()
    keys = pygame.key.get_pressed()

    player.move(keys)
    player.color(keys)
    player.size(keys)

    screen.fill(WHITE)
    player.draw(screen)
    pygame.display. flip()

pygame. quit()
sys.exit()