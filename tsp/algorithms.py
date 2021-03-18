from typing import List, Tuple
from tsp.utils import euclidean_distance, get_route_distance
import numpy as np


def simulated_annealing():
    print("Simmulated Annealing")


def should_edges_swap(
    routes: List[Tuple[int, int]],
    index_a: int,
    index_b: int
) -> bool:
    current_distance = (
        euclidean_distance(routes[index_a], routes[index_a - 1]),
        euclidean_distance(routes[index_b], routes[index_b - 1])
    )
    swapped_distance = (
        euclidean_distance(routes[index_a], routes[index_b]),
        euclidean_distance(routes[index_a - 1], routes[index_b - 1])
    )

    if sum(swapped_distance) < sum(current_distance):
        lower = min(index_a, index_b)
        higher = max(index_a, index_b)

        routes[lower:higher] = routes[lower:higher][::-1]

        return True
    return False
