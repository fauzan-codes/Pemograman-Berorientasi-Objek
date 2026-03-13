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

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)



class Polisi(Character):
    def move(self,keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
                self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += self.speed

class Maling (Character):
    def move(self,keys):
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_d] and self.x < WIDTH - self.width:
            self.x += self.speed
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_s] and self.y < HEIGHT - self.height:
            self.y += self.speed


polisi = Polisi( 100, 200, BLUE)
maling = Maling( 400, 200, RED)


running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:
        polisi.move(keys)
        maling.move(keys)


    screen.fill(WHITE)

    if polisi.get_rect().colliderect(maling.get_rect()):
        # print("Polisi Menang!")
        # running = False
        game_over = True

    if game_over:
        font = pygame.font.SysFont(None, 48)
        text = font.render("POLISI MENANG", True, (0, 0, 0))
        screen.blit(text, (170, 180))

    polisi.draw(screen)
    maling.draw(screen)

    pygame.display.update()


screen.fill((0, 0, 0))
font = pygame.font.SysFont(None, 48)
text = font.render("POLISI MENANG", True, (255, 255, 255))

pygame.quit()
sys.exit()



