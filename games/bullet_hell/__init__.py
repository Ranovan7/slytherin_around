import sys
import random
from typing import List

import pygame
from pygame.locals import *
from pygame.math import Vector2 as vec

from games.bullet_hell.player import Player
from games.bullet_hell.spawner import (
    Spawner,
    HorizontalLineSpawner,
    VerticalLineSpawner,
    FireworkSpawner,
    DelayedSpawner
)
from games.bullet_hell.bullet import HomingBullet
from games.bullet_hell.utils import add_sprites
from games.bullet_hell.master import *

SPAWNER_LIST = [
    HorizontalLineSpawner,
    VerticalLineSpawner,
    FireworkSpawner,
    DelayedSpawner
]


class BulletHell:
    sprites: pygame.sprite.Group
    spawners: List[Spawner]
    player: Player

    def __init__(self):
        self.player = Player()
        self.sprites = pygame.sprite.Group()
        self.spawners = []
        self.framecount = 100
        self.frametrigger = 100

        self.add_sprites([self.player])

    def add_sprites(self, sprites):
        for sprite in sprites:
            self.sprites.add(sprite)

    def generate_spawner(self):
        self.framecount += 1
        if self.framecount >= self.frametrigger:
            SpawnerObj = random.choice(SPAWNER_LIST)
            spawner = SpawnerObj(
                (
                    random.randint(0, WIDTH),
                    random.randint(0, HEIGHT)
                )
            )

            if spawner.Bullet == HomingBullet:
                print("Bullet is Homing Bullet")
                spawner.target = self.player.position

            self.add_spawner(spawner)
            spawner.announce()

            self.framecount = 0

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

        gamedata.generate_spawner()
        gamedata.update()
        gamedata.count_sprites()

        pygame.display.update()
        FramePerSec.tick(FPS)
