import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Kejar Maling")

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

class Character:
    def __init__ (self, x, y, color):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 0.5
        self.color = color

    # 2 usages
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    # 2 usages
    def get_rect(self):
        return pygame. Rect(self.x, self.y, self.width, self.height)



class Polisi(Character):
    # 1 usage
    def move(self,keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
                self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

class Maling (Character):
    # 1 usage
    def move(self,keys):
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed


polisi = Polisi( 100, 200, BLUE)
maling = Maling( 400, 200, RED)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            running = False

keys = pygame.key.get_pressed()

polisi.move(keys)
maling.move(keys)

if polisi.get_rect().colliderect(maling.get_rect()):
    print("Polisi Menang!")
    running = False

screen.fill(WHITE)

polisi.draw(screen)
maling.draw(screen)

pygame.display. update()

pygame.quit()
sys.exit()



