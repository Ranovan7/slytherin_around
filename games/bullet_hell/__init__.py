import sys
import random
from typing import List

import pygame
from pygame.locals import *
from pygame.math import Vector2 as vec

from games.bullet_hell.player import Player
from games.bullet_hell.spawner import HorizontalLineSpawner
from games.bullet_hell.utils import add_sprites
from games.bullet_hell.master import *


def main():
    print("Starting...")

    pygame.init()

    FramePerSec = pygame.time.Clock()

    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")

    P1 = Player()

    all_sprites = pygame.sprite.Group()
    add_sprites(all_sprites, [P1])

    S1 = HorizontalLineSpawner((random.randint(WIDTH, HEIGHT), random.randint(WIDTH, HEIGHT)))
    add_sprites(all_sprites, S1.get_sprites())
    S1.announce()

    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        displaysurface.fill((0,0,0))

        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)

        S1.update()
        P1.update()

        pygame.display.update()
        FramePerSec.tick(FPS)
