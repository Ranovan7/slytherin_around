import random
import numpy as np
from typing import List

from boids.utils import euclidean_distance, set_mag


class Bird:
    position:(int, int)
    velocity:(int, int)
    acceleration:(int, int)
    perception_rad: float = 100.0
    min_speed: float = 5.0
    max_speed: float = 10.0
    acc_limit: float = 2.0

    def __init__(self, position: (int, int)):
        self.position = position
        self.velocity = np.array([random.randint(-10.0, 10.0), random.randint(-10.0, 10.0)])
        self.acceleration = np.array([0.0, 0.0])

    def wrap(self, width, height):
        if self.position[0] > width:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = width

        if self.position[1] > height:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = height

    def update(self):
        self.velocity = np.add(self.velocity, self.acceleration)
        self.velocity = np.clip(self.velocity, a_min = -self.max_speed, a_max = self.max_speed)
        self.position = np.add(self.position, self.velocity)

    def emergence(self, birds: List):
        self.acceleration = np.array([0.0, 0.0])
        steer_align = np.array([0.0, 0.0])
        steer_cohesion = np.array([0.0, 0.0])
        steer_separation = np.array([0.0, 0.0])
        close = 0
        for bird in birds:
            if bird == self:
                continue

            distance = self.distance(bird)
            if distance <= self.perception_rad:
                close += 1
                steer_align = np.add(steer_align, bird.velocity)
                steer_cohesion = np.add(steer_cohesion, bird.position)

                diff = np.subtract(self.position, bird.position)
                diff = diff / (distance**2)
                steer_separation = np.add(steer_separation, diff)

        if close > 0:
            steer_align = steer_align / close
            steer_align = set_mag(steer_align, self.min_speed)
            steer_align = np.subtract(steer_align, self.velocity)

            steer_cohesion = steer_cohesion / close
            steer_cohesion = np.subtract(steer_cohesion, self.position)
            steer_cohesion = set_mag(steer_cohesion, self.min_speed)
            steer_cohesion = np.subtract(steer_cohesion, self.velocity)

            steer_separation = steer_separation / close
            steer_separation = set_mag(steer_separation, self.min_speed)
            steer_separation = np.subtract(steer_separation, self.velocity)

        self.acceleration += np.clip(steer_align, a_min = -self.acc_limit, a_max = self.acc_limit)
        self.acceleration += np.clip(steer_cohesion, a_min = -self.acc_limit, a_max = self.acc_limit)
        self.acceleration += np.clip(steer_separation, a_min = -self.acc_limit, a_max = self.acc_limit)

    def align(self, birds: List):
        steering = np.array([0.0, 0.0])
        close = 0
        for bird in birds:
            if bird == self:
                continue

            if self.distance(bird) <= self.perception_rad:
                close += 1
                steering = np.add(steering, bird.velocity)

        if close > 0:
            steering = steering / close
            steering = set_mag(steering, self.min_speed)
            steering = np.subtract(steering, self.velocity)

        self.acceleration = np.clip(steering, a_min = -self.acc_limit, a_max = self.acc_limit)

    def cohesion(self, birds: List):
        steering = np.array([0.0, 0.0])
        close = 0
        for bird in birds:
            if bird == self:
                continue

            if self.distance(bird) <= self.perception_rad:
                close += 1
                steering = np.add(steering, bird.position)

        if close > 0:
            steering = steering / close
            steering = np.subtract(steering, self.position)
            steering = set_mag(steering, self.min_speed)
            steering = np.subtract(steering, self.velocity)

        self.acceleration = np.clip(steering, a_min = -self.acc_limit, a_max = self.acc_limit)

    def separation(self, birds: List):
        steering = np.array([0.0, 0.0])
        close = 0
        for bird in birds:
            if bird == self:
                continue

            distance = self.distance(bird)
            if distance <= self.perception_rad:
                close += 1
                diff = np.subtract(self.position, bird.position)
                diff = diff / (distance**2)
                steering = np.add(steering, diff)

        if close > 0:
            steering = steering / close
            # steering = np.subtract(steering, self.position)
            steering = set_mag(steering, self.min_speed)
            steering = np.subtract(steering, self.velocity)

        self.acceleration = np.clip(steering, a_min = -self.acc_limit, a_max = self.acc_limit)

    def distance(self, bird):
        return euclidean_distance(self.position, bird.position)


class Flock:

    def __init__(
        self,
        n_birds: int = 30,
        border: int = 1000
    ):
        self.birds: List[(int, int)] = []
        self.border = border
        for _ in range(n_birds):
            self.birds.append(
                Bird(np.array(
                    [
                        random.randint(0.0, float(border)),
                        random.randint(0.0, float(border))
                    ]
                ))
            )

    def update(self):
        for bird in self.birds:
            bird.wrap(self.border, self.border)
            # bird.align(self.birds)
            # bird.cohesion(self.birds)
            # bird.separation(self.birds)
            bird.emergence(self.birds)
            bird.update()

    def get_frame(self):
        return [bird.position for bird in self.birds]
