import random
import numpy as np
from typing import List

from boids.utils import euclidean_distance, set_mag


class Bird:
    position:(int, int, int)
    velocity:(int, int, int)
    acceleration:(int, int, int)
    alignment_rad: float = 100.0
    cohesion_rad: float = 150.0
    separation_rad: float = 100.0
    min_speed: float = 10.0
    max_speed: float = 15.0
    acc_limit: float = 3.0

    def __init__(self, position: (int, int, int), velocity: (int, int, int), id: int = None):
        self.position = position
        self.velocity = velocity
        self.acceleration = np.array([0.0, 0.0, 0.0])
        self.id = id

    def get_frame(self, dim: str = '2d'):
        if dim == '2d':
            return self.position[:2]
        else:
            return self.position

    def wrap(self, width, height, depth):
        if self.position[0] > width:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = width

        if self.position[1] > height:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = height

        if self.position[2] > depth:
            self.position[2] = 0
        elif self.position[2] < 0:
            self.position[2] = depth

    def reset_acceleration(self):
        self.acceleration = np.array([0.0, 0.0, 0.0])

    def add_force(self, force):
        force = np.clip(force, a_min = -self.acc_limit, a_max = self.acc_limit)
        self.acceleration = np.add(self.acceleration, force)
        # self.acceleration = np.clip(self.acceleration, a_min = -self.acc_limit, a_max = self.acc_limit)

    def update(self):
        self.velocity = np.add(self.velocity, self.acceleration)
        self.velocity = np.clip(self.velocity, a_min = -self.max_speed, a_max = self.max_speed)
        self.position = np.add(self.position, self.velocity)
        # print(f"Bird {self.id} - {self.velocity}")

    def emergence(self, birds: List):
        # self.reset_acceleration()
        steer_align = np.array([0.0, 0.0, 0.0])
        steer_cohesion = np.array([0.0, 0.0, 0.0])
        steer_separation = np.array([0.0, 0.0, 0.0])
        count_align = 0
        count_cohesion = 0
        count_separation = 0

        for bird in birds:
            if bird == self:
                continue

            distance = self.distance(bird)
            if distance <= self.alignment_rad:
                count_align += 1
                steer_align = np.add(steer_align, bird.velocity)

            if distance <= self.cohesion_rad:
                count_cohesion += 1
                steer_cohesion = np.add(steer_cohesion, bird.position)

            if distance <= self.separation_rad:
                count_separation += 1
                diff = np.subtract(self.position, bird.position)
                diff = diff / (distance * distance)
                steer_separation = np.add(steer_separation, diff)

        if count_align > 0:
            steer_align = steer_align / count_align
            steer_align = set_mag(steer_align, self.min_speed)
            steer_align = np.subtract(steer_align, self.velocity)

        if count_cohesion > 0:
            steer_cohesion = steer_cohesion / count_cohesion
            steer_cohesion = np.subtract(steer_cohesion, self.position)
            steer_cohesion = set_mag(steer_cohesion, self.min_speed)
            steer_cohesion = np.subtract(steer_cohesion, self.velocity)

        if count_separation > 0:
            steer_separation = steer_separation / count_separation
            steer_separation = set_mag(steer_separation, self.min_speed)
            steer_separation = np.subtract(steer_separation, self.velocity)

        self.add_force(steer_align)
        self.add_force(steer_cohesion)
        self.add_force(steer_separation)

    def distance(self, bird):
        return euclidean_distance(self.position, bird.position)


class Flock:

    def __init__(
        self,
        n_birds: int = 30,
        dim: str = '2d',
        border: int = 1000
    ):
        self.birds: List[(int, int)] = []
        self.border = border
        for i in range(n_birds):
            self.birds.append(
                Bird(
                    position = np.array(
                        [
                            random.randint(0.0, float(border)),
                            random.randint(0.0, float(border)),
                            0.0 if dim == '2d' else random.randint(0.0, float(border))
                        ]
                    ),
                    velocity = np.array(
                        [
                            random.randint(-10.0, 10.0),
                            random.randint(-10.0, 10.0),
                            0.0 if dim == '2d' else random.randint(-10.0, 10.0)
                        ]
                    ),
                    id = i
                )
            )

    def update(self):
        for bird in self.birds:
            bird.wrap(self.border, self.border, self.border)
            bird.reset_acceleration()

            bird.emergence(self.birds)

            bird.update()

    def get_frame(self, dim: str = '2d'):
        return [bird.get_frame(dim=dim) for bird in self.birds]
