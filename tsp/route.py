from typing import List
from random import shuffle
from tsp.utils import euclidean_distance, get_all_possible_pairings
import numpy as np


class Route:
    routes: np.ndarray    # List[(int, int)]
    pairings: np.ndarray    # List[(int, int)]

    def __init__(self, cities):
        self.routes = cities
        self.pairings = get_all_possible_pairings(self.routes)

    def total_distance(self) -> float:
        distance = 0
        for i, route in enumerate(self.routes):
            distance += euclidean_distance(route, self.routes[i-1])
        return round(distance, 2)

    def possible_pairings(self):
        shuffle(self.pairings)
        return self.pairings

    def should_edges_swap(self, index_a: int, index_b: int) -> bool:
        if not self.check_swap_viability(index_a, index_b):
            return False

        current_distance = (
            euclidean_distance(self.routes[index_a], self.routes[index_a - 1]),
            euclidean_distance(self.routes[index_b], self.routes[index_b - 1])
        )
        swapped_distance = (
            euclidean_distance(
                self.routes[index_a],
                self.routes[index_b]),
            euclidean_distance(
                self.routes[index_a - 1],
                self.routes[index_b - 1])
        )

        if sum(swapped_distance) < sum(current_distance):
            lower = min(index_a, index_b)
            higher = max(index_a, index_b)

            self.routes[lower:higher] = self.routes[lower:higher][::-1]

            return True
        return False

    def check_swap_viability(self, index_a: int, index_b: int) -> bool:
        if abs(index_a - index_b) == 1:
            return False

        if 0 in [index_a, index_b] and len(self.routes) - 1 in [index_a, index_b]:
            return False

        return True
