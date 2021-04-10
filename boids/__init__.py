from typing import List
from random import randint, choice

from boids.flock import Flock
from boids.utils import animate_frames


def bird_flocks(border: int = 1000, n_frames: int = 700, saves: str = None):
    frames = []
    flock = Flock()

    for i in range(n_frames):
        flock.update()
        # print(skill.get_frame())
        frames.append(flock.get_frame())

    animate_frames(frames, border, saves)
