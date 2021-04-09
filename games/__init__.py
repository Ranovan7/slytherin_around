import sys
from typing import List

import pygame
from pygame.locals import *
from pygame.math import Vector2 as vec

HEIGHT = 900
WIDTH = 800
ACC = 0.5
FRIC = -0.12
FPS = 60


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: List[int] = (400,400), size: int = 30):
        super().__init__()
        self.surf = pygame.Surface((size, size))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()

        self.pos = vec(pos)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.horizontal_limit = self.surf.get_width()/2

    def move(self):
        self.acc = vec(0,0)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        if pressed_keys[K_UP]:
            self.acc.y = -ACC
        if pressed_keys[K_DOWN]:
            self.acc.y = ACC

        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH - self.horizontal_limit:
            self.pos.x = WIDTH - self.horizontal_limit
        if self.pos.x < self.horizontal_limit:
            self.pos.x = self.horizontal_limit
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        if self.pos.y < self.surf.get_height():
            self.pos.y = self.surf.get_height()

        self.rect.midbottom = self.pos


def platformers():
    print("Starting...")

    pygame.init()
    vec = pygame.math.Vector2

    FramePerSec = pygame.time.Clock()

    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")

    P1 = Player()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        displaysurface.fill((0,0,0))

        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)

        P1.move()

        pygame.display.update()
        FramePerSec.tick(FPS)
