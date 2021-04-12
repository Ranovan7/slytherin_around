import time
from typing import List
from random import randint, choice

from boids.flock import Flock
from boids.utils import animate_frames
from nimrod import boids


def bird_flocks(
    n_birds: int = 50,
    lang: str = 'py',
    n_frames: int = 700,
    saves: str = None
):
    if lang not in ['py', 'nim']:
        print("Programming Language Not Supported")
        return

    border = 2000
    frames = []
    start = time.time()

    if lang == 'py':
        flock = Flock(n_birds, border)

        for i in range(n_frames):
            flock.update()
            frames.append(flock.get_frame())
    elif lang == 'nim':
        frames = boids.simulation(n_birds, border, n_frames)

    print(f"Emulating {n_frames} frames on {round(time.time() - start, 2)} seconds")

    animate_frames(frames, border, saves)
