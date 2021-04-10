import math
from typing import List

import pygame


def add_sprites(sprites_group: pygame.sprite.Group, sprites):
    for sprite in sprites:
        sprites_group.add(sprite)


def get_vectors_angle(angle: int, speed: int) -> List[List[int]]:
    movement = [
        speed * math.sin(math.radians(angle)),
        speed * math.cos(math.radians(angle))
    ]
    return movement


def get_radians_from_points(p1: List[int], p2: List[int]):
    return math.degrees(math.atan2(p2[0] - p1[0], p2[1] - p1[1]))
