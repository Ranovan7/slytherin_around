import sys
import random
from typing import List

import pygame
from pygame.locals import *
from pygame.math import Vector2 as vec

from games.utils import add_sprites
from games.boids.birds import Player, Bird
from games.boids.master import *


class BoidsSimulation:
    birds: pygame.sprite.Group
    player: Player

    def __init__(self):
        self.player = Player()
        self.sprites = pygame.sprite.Group()
        self.birds = []

        self.add_sprites([self.player])

    def add_sprites(self, sprites):
        for sprite in sprites:
            self.sprites.add(sprite)

    def update(self):
        for birds in self.birds:
            birds.update()

        self.player.update()

    def count_sprites(self):
        print(f"Sprites Count : {len(self.sprites)}")

    def all_birds(self):
        return self.birds + self.player


def main():
    print("Starting...")

    pygame.init()

    FramePerSec = pygame.time.Clock()

    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")

    gamedata = BoidsSimulation()

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

        pygame.display.update()
        FramePerSec.tick(FPS)
