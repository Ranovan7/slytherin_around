from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math


def euclidean_distance(a, b):
    return((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5


def set_mag(vec, new_mag):
    mag = math.sqrt(vec[0]**2 + vec[1]**2)
    if mag == 0:
        return np.array([0, 0])
    return np.array([(vec[0] * new_mag)/mag, (vec[1] * new_mag)/mag])


def create_frames(
    bullets: List[Tuple[int, int]]
) -> Tuple[List[int], List[int]]:
    x = [b[0] for b in bullets]
    y = [b[1] for b in bullets]
    return x, y


def animate_frames(
    frames: List[Tuple[List[int], List[int]]],
    border: int,
    saves: str = None
):
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(xlim=(0, border), ylim=(0, border))
    scatter = plt.scatter([], [], s=30, c='r')

    def animate(i):
        scatter.set_offsets(frames[i])
        return scatter,

    plt.xticks([])
    plt.yticks([])
    ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, frames=len(frames), repeat=False)

    if saves:
        print("saving results...")
        ani.save(f"./boids/examples/{saves}.gif")

    plt.show()
