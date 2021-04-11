import math
from typing import List

import pygame


def add_sprites(sprites_group: pygame.sprite.Group, sprites):
    for sprite in sprites:
        sprites_group.add(sprite)
