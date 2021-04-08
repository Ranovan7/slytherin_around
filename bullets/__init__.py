from typing import List
from random import randint, choice
from bullets.spawner import HorizontalLineSpawner, VerticalLineSpawner, FireworkSpawner, DelayedSpawner
from bullets.utils import animate_frames, create_frames

spawners = [
    HorizontalLineSpawner,
    VerticalLineSpawner,
    FireworkSpawner,
    FireworkSpawner,
    DelayedSpawner,
    DelayedSpawner
]


def bullet_hell(border: int = 1000, n_frames: int = 700, saves: str = None):
    frames = []
    skill = None

    for i in range(n_frames):
        if not skill or i % 70 == 0:
            if n_frames - i >= 70:
                Spawner = choice(spawners)
                skill = Spawner((randint(200, border), randint(200, border)))
                skill.announce()

        skill.update()
        # print(skill.get_frame())
        frames.append(skill.get_frame())

    animate_frames(frames, border, saves)
