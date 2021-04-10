import sys
import random
from typing import List

import pygame
from pygame.locals import *
from pygame.math import Vector2 as vec

from games.bullet_hell.player import Player
from games.bullet_hell.spawner import Spawner, HorizontalLineSpawner
from games.bullet_hell.utils import add_sprites
from games.bullet_hell.master import *


class BulletHell:
    sprites: pygame.sprite.Group
    spawners: List[Spawner]
    player: Player

    def __init__(self):
        self.player = Player()
        self.sprites = pygame.sprite.Group()
        self.spawners = []

        self.add_sprites([self.player])

    def add_sprites(self, sprites):
        for sprite in sprites:
            self.sprites.add(sprite)

    def generate_spawner(self):
        spawner = HorizontalLineSpawner(
            (
                random.randint(WIDTH, HEIGHT),
                random.randint(WIDTH, HEIGHT)
            )
        )
        self.add_spawner(spawner)
        spawner.announce()

    def add_spawner(self, spawner):
        self.spawners.append(spawner)
        self.add_sprites(spawner.get_sprites())

    def update(self):
        for spawner in self.spawners:
            spawner.update()

        self.player.update()

    def count_sprites(self):
        print(f"Sprites Count : {len(self.sprites)}")


def main():
    print("Starting...")

    pygame.init()

    FramePerSec = pygame.time.Clock()

    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")

    gamedata = BulletHell()
    gamedata.generate_spawner()

    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        displaysurface.fill((0,0,0))

        for entity in gamedata.sprites:
            displaysurface.blit(entity.surf, entity.rect)

        gamedata.update()
        gamedata.count_sprites()

        pygame.display.update()
        FramePerSec.tick(FPS)
