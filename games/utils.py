import math
from typing import List

import pygame
from pygame.math import Vector2


def add_sprites(sprites_group: pygame.sprite.Group, sprites):
    for sprite in sprites:
        sprites_group.add(sprite)


def euclidean_distance(a, b):
    return ((b.x - a.x)**2 + (b.y - a.y)**2)**0.5


def set_mag(vec, new_mag):
    mag = math.sqrt(vec.x**2 + vec.y**2)
    if mag == 0:
        return Vector2(0, 0)
    return Vector2((vec.x * new_mag)/mag, (vec.y * new_mag)/mag)


def vec_clip(vec, a_min, a_max):
    vec.x = min(a_max, max(vec.x, a_min))
    vec.y = min(a_max, max(vec.y, a_min))
    return vec
