from typing import List, Tuple
from random import randint, shuffle
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import itertools


def euclidean_distance(a: Tuple[int, int], b: Tuple[int, int]):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


def generate_cities(
    n_city: int = 20,
    border: int = 1000
) -> List[Tuple[int, int]]:
    return [(randint(0, border), randint(0, border)) for i in range(n_city)]


def get_all_possible_pairings(
    cities: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    results = list(itertools.combinations(range(len(cities)), 2))
    shuffle(results)
    return results


def create_plot(routes: List[Tuple[int, int]]) -> (List[int], List[int]):
    x = [routes[r % len(routes)][0] for r in range(len(routes) + 1)]
    y = [routes[r % len(routes)][1] for r in range(len(routes) + 1)]
    return x, y


def animate_plot(plots, border: int, saves: str = None):
    fig = plt.figure()
    dev = round(border * 0.05)
    ax = plt.axes(xlim=(0 - dev, border + dev), ylim=(0 - dev, border + dev))
    line, = ax.plot([], [], lw=2)

    for i in range(10):
        plots.append(plots[-1])

    def animate(i):
        line.set_data(plots[i][0], plots[i][1])
        return line,

    ani = animation.FuncAnimation(fig, animate, interval=100, blit=True, frames=len(plots), repeat=False)

    if saves:
        print("saving results...")
        ani.save(f"./tsp/examples/{saves}.gif")
    plt.show()
