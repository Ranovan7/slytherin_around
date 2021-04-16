from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math


def euclidean_distance(a, b):
    return((b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2)**0.5


def set_mag(vec, new_mag):
    mag = math.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
    if mag == 0:
        return np.array([0, 0, 0])
    return np.array([(vec[0] * new_mag)/mag, (vec[1] * new_mag)/mag, (vec[2] * new_mag)/mag])


def animate_2d_frames(
    frames: List[Tuple[List[int], List[int], List[int]]],
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


def animate_3d_frames(
    frames: List[Tuple[List[int], List[int], List[int]]],
    border: int,
    saves: str = None
):
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    # Fifty lines of random 3-D lines
    data = [Gen_RandLine(25, 3) for index in range(50)]

    # Creating fifty line objects.
    # NOTE: Can't pass empty arrays into 3d version of plot()
    scatters = [ ax.scatter(data[0][i,0:1], data[0][i,1:2], data[0][i,2:]) for i in range(data[0].shape[0]) ]

    # Setting the axes properties
    ax.set_xlim3d([0.0, 1.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 1.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 1.0])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')

    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
                                       interval=50, blit=False)

    plt.show()

    if saves:
        print("saving results...")
        ani.save(f"./boids/examples/{saves}.gif")

    plt.show()
