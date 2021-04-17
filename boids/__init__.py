import time
import numpy as np
from typing import List
from random import randint, choice

from boids.flock import Flock
from boids.utils import animate_2d_frames, animate_3d_frames
from nimrod import boids


def bird_flocks(
    n_birds: int = 50,
    lang: str = 'py',
    dim: str = '2d',
    n_frames: int = 700,
    saves: str = None
):
    if lang not in ['py', 'nim']:
        print("Programming Language Not Supported")
        return

    if dim not in ['2d', '3d']:
        print("Dimension Not Supported")
        return

    border = 2000
    frames = []
    start = time.time()

    if lang == 'py':
        flock = Flock(n_birds, dim, border)
        for i in range(n_frames):
            flock.update()
            frames.append(flock.get_frame(dim=dim))

    elif lang == 'nim':
        frames = boids.simulation(n_birds, dim, border, n_frames)

    print(f"Emulating {n_frames} frames on {round(time.time() - start, 2)} seconds")

    if dim == "2d":
        animate_2d_frames(frames, border, saves)
    elif dim == "3d":
        animate_3d_frames(np.array(frames), border, saves)
