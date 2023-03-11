import pygame
from pygame.locals import *
import sys
import random

pygame.init()

vec = pygame.math.Vector2
HEIGHT = 750
WIDTH = 800
ACC = 0.5
FRIC = -0.12
FPS = 60
FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class Baseplate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))

class Platform1(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.surf = pygame.Surface((height, width))
        self.surf.fill((200, 110, 30))
        self.rect = self.surf.get_rect(center=(x, y))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect()

        self.pos = vec((200, 400))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)



# Гравитация (второй параметр в vec)
    def update(self):
        self.acc = vec(0, 0.3)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_d]:
            self.acc.x = ACC
        if pressed_keys [K_SPACE]:
            self.vel.y = -10

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

class Booster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((38, 255, 40))
        self.rect = self.surf.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = 200

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
players = pygame.sprite.Group()
booster = pygame.sprite.Group()

boost = Booster()
BP = Baseplate()
P1 = Player()
PT1 = Platform1(100, 20, 100, 250)
PT2 = Platform1(30, 120, 300, 450)

platforms.add(BP)
platforms.add(PT1)
platforms.add(PT2)

all_sprites.add(BP)
all_sprites.add(P1)
all_sprites.add(PT1)
all_sprites.add(PT2)
all_sprites.add(boost)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill((0, 0, 0))
    hits = pygame.sprite.groupcollide(P1, platforms, False)
    if hits:
        P1.pos.y = hits[0].rect.top + 1
        P1.vel.y = 0
#Доделать бонусы (гравитация)
    hits = pygame.sprite.groupcollide(P1, booster, False)
    if hits:
        P1.pos.y = hits[0].rect.top + 1
        P1.vel.y = 0
    P1.update()
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
#