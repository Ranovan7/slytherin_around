import time
from typing import List
from random import randint, choice

from boids.flock import Flock
from boids.utils import animate_frames


def bird_flocks(
    n_birds: int = 50,
    border: int = 1000,
    n_frames: int = 700,
    saves: str = None
):
    frames = []
    flock = Flock(n_birds, border)
    start = time.time()

    for i in range(n_frames):
        flock.update()
        # print(skill.get_frame())
        frames.append(flock.get_frame())
    print(f"Emulating {n_frames} frames on {round(time.time() - start, 2)} seconds")

    animate_frames(frames, border, saves)
