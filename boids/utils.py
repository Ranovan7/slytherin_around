from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math


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
    fig = plt.figure()
    dev = round(border * 0.05)
    ax = plt.axes(xlim=(0 - dev, border + dev), ylim=(0 - dev, border + dev))
    scatter = plt.scatter([], [], s=30, c='r')

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
