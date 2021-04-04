from typing import List
from random import randint, choice
from bullets.spawner import BaseSpawner, CurveSpawner, BaseFireworks
from bullets.utils import animate_frames, create_frames

spawners = [
    BaseSpawner,
    CurveSpawner,
    BaseFireworks
]


def bullet_hell(border: int = 1000, n_frames: int = 500, saves: str = None):
    frames = []
    skill = None

    for i in range(n_frames):
        if not skill or (i + 1) % 50 == 0:
            Spawner = choice(spawners)
            skill = Spawner((randint(200, border), randint(200, border)))
            print(f"Spawn {Spawner}")

        skill.update()
        # print(skill.get_frame())
        frames.append(skill.get_frame())

    animate_frames(frames, border, saves)
