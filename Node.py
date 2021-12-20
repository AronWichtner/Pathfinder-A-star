import random
from Grid import *

g = Grid()


def choose_obstacle_value():
    states = [0, 1]
    probability = [0.6, 0.4]
    return random.choices(states, probability)[0]


class Node:

    def __init__(self, x, y, parent):
        self.f = 0
        self.g = 0
        self.h = 0
        self.coordinates = [x, y]
        if self.coordinates == [0, 0] or self.coordinates == [g.grid_width - 1, g.grid_height - 1]:
            self.value = 0
        else:
            self.value = choose_obstacle_value()
        self.parent = parent
