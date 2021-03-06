from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math


def update(gen):
    return next(gen)


def get_vectors_angle(angle: int, speed: int) -> List[List[int]]:
    movement = [
        speed * math.sin(math.radians(angle)),
        speed * math.cos(math.radians(angle))
    ]
    return movement


def get_radians_from_points(p1: List[int], p2: List[int]):
    return math.degrees(math.atan2(p2[0] - p1[0], p2[1] - p1[1]))


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
    dev = round(border * 0.05)
    ax = plt.axes(xlim=(0 - dev, border + dev), ylim=(0 - dev, border + dev))
    scatter = plt.scatter([], [], s=70, c='r')

    def animate(i):
        scatter.set_offsets(frames[i])
        return scatter,

    plt.xticks([])
    plt.yticks([])
    ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, frames=len(frames), repeat=False)

    if saves:
        print("saving results...")
        ani.save(f"./bullets/examples/{saves}.gif")

    plt.show()
