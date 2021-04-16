from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
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
    ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, frames=len(frames), repeat=True)

    if saves:
        print("saving results...")
        ani.save(f"./boids/examples/{saves}.gif")

    plt.show()


def animate_3d_frames(
    data,
    border: int,
    saves: str = None
):
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    # Setting the axes properties
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim3d(0, border)
    ax.set_ylim3d(0, border)
    ax.set_zlim3d(0, border)
    ax.set_title('3D Boids')

    # Creating fifty line objects.
    # NOTE: Can't pass empty arrays into 3d version of plot()
    scatters = [ax.scatter(data[0][i,0:1], data[0][i,1:2], data[0][i,2:], c='b') for i in range(data[0].shape[0])]

    def animate_graph(n_iter, data, scatters):
        for i in range(data[0].shape[0]):
            scatters[i]._offsets3d = (data[n_iter][i,0:1], data[n_iter][i,1:2], data[n_iter][i,2:])
        return scatters

    # Creating the Animation object
    ani = animation.FuncAnimation(fig, animate_graph, len(data), fargs=(data, scatters),
                                       interval=20, repeat=True)

    if saves:
        print("saving results...")
        ani.save(f"./boids/examples/{saves}.gif")

    plt.show()
