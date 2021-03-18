import numpy as np
import random
import time
from tsp.utils import *
from tsp.algorithms import calculate_edges_swap


def travelling_salesman(n_city: int = 30, border: int = 1000, saves: str = None, loop_limit: int = None):
    if n_city <= 3:
        print("City samples too few!")
        return

    start = time.time()
    cities = np.array(generate_cities(n_city, border))
    routes = cities
    plots = []

    print(f"Current Distance : {get_route_distance(routes)}")
    print("Calculating...")
    i = 0
    while True:
        i += 1
        maxed = False
        pairings = get_all_possible_pairings(routes)

        for pair in pairings:
            if check_swap_viability(pair[0], pair[1]):
                maxed = calculate_edges_swap(routes, pair[0], pair[1])

                if maxed:
                    plots.append((create_plot(routes)))
                    break

        if not maxed or (loop_limit and i >= loop_limit):
            break

    print(f"Finish at {round(time.time() - start, 3)} seconds")
    print(f"Best Distance Results : {get_route_distance(routes)}")
    animate_plot(plots, border, saves)
