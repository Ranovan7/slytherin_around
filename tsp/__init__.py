import numpy as np
import random
import time
from tsp.utils import *
from tsp.route import Route


def travelling_salesman(n_city: int = 30, border: int = 1000, saves: str = None, loop_limit: int = None):
    if n_city <= 3:
        print("City samples too few!")
        return

    start = time.time()
    cities = np.array(generate_cities(n_city, border))
    route = Route(cities)
    plots = []

    print(f"Current Distance : {route.total_distance()}")
    print("Calculating...")
    i = 0
    while True:
        i += 1
        swapped = False

        for pair in route.possible_pairings():
            swapped = route.should_edges_swap(pair[0], pair[1])

            if swapped:
                plots.append(create_plot(route.routes))
                break

        if not swapped or (loop_limit and i >= loop_limit):
            break

    print(f"Finish at {round(time.time() - start, 3)} seconds")
    print(f"Best Distance Results : {route.total_distance()}")
    animate_plot(plots, border, saves)
