from typing import List, Tuple
from collections.abc import Iterator
import numpy as np
import random
import math

from games.platformers.master import *
from games.platformers.utils import get_vectors_angle
from games.platformers.bullet import Bullet, LinearBullet, TurningBullet, OscilatingBullet, HomingBullet

LINE_BULLETS = [LinearBullet, OscilatingBullet]
FIREWORK_BULLETS = [LinearBullet, TurningBullet, HomingBullet]


class Spawner:
    bullets: List[Bullet] = []
    speed: int = 20

    def update(self):
        for bullet in self.bullets:
            bullet.update()

    def get_sprites(self) -> Tuple[List[int], List[int]]:
        return self.bullets

    def announce(self):
        print(f"{self.__class__.__name__} spawning {self.bullets[0].__class__.__name__}")


class HorizontalLineSpawner(Spawner):

    def __init__(self, location: Tuple[int, int]):
        self.bullets = []
        self.Bullet = random.choice(LINE_BULLETS)

        y = 0
        self.angle = 0
        if random.randint(0, 1) == 1:
            y = 1000
            self.angle = 180

        multiplier = 200
        for i in range(7):
            self.bullets.append(self.Bullet(
                position=np.array([-100 + (multiplier*i), y]),
                speed=self.speed,
                angle=self.angle
            ))


class VerticalLineSpawner(Spawner):

    def __init__(self, location: Tuple[int, int]):
        self.bullets = []
        self.Bullet = random.choice(LINE_BULLETS)

        x = 0
        self.angle = 90
        if random.randint(0, 1) == 1:
            x = 1000
            self.angle = 270

        multiplier = 200
        for i in range(7):
            self.bullets.append(self.Bullet(
                position=np.array([x, -100 + (multiplier*i)]),
                speed=self.speed,
                angle=self.angle
            ))


class FireworkSpawner(Spawner):

    def __init__(self, location: Tuple[int, int] = None, n_bullets: int = 8):
        self.bullets = []
        self.location = location
        self.Bullet = random.choice(FIREWORK_BULLETS)

        if not self.location:
            self.location = [0, 500]

        multiplier = 360/n_bullets
        for i in range(n_bullets):
            angle = multiplier * i
            self.bullets.append(self.Bullet(
                position=np.array(self.location),
                speed=self.speed,
                angle=angle
            ))


class DelayedSpawner(Spawner):

    def __init__(self, location: Tuple[int, int] = None, angle: int = 45):
        self.bullets = []
        self.location = location
        self.angle = angle
        self.frame_count = 0
        self.Bullet = random.choice(FIREWORK_BULLETS)

        if not self.location:
            self.location = [0, 500]

        self.add_bullet()

    def update(self):
        self.frame_count += 1
        for bullet in self.bullets:
            bullet.update()

        if self.frame_count % 7 == 0:
            self.add_bullet()

    def add_bullet(self):
        self.bullets.append(self.Bullet(
            position=np.array(self.location),
            speed=self.speed,
            angle=self.angle * len(self.bullets)
        ))
