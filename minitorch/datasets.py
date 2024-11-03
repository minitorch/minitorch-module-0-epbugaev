import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N):
    """Generate N 2d points with coordinates between 0.0 and 1.0

    Args:
    ----
        N: number of points

    Returns:
    -------
        List of tuples with points' coordinates

    """
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    """A Graph is a number of 2d points with y values. 
    """
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N):
    """Assign y according to the following rule: 
    1s are points left to x=0.5, 0s are points right to 0.5

    Args:
    ----
        N: number of points

    Returns:
    -------
        Graph with assigned y values

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N):
    """Assign y according to the following rule: 
    1s below line x + y = 1, 0s above. 

    Args:
    ----
        N: number of points

    Returns:
    -------
        Graph with assigned y values

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N):
    """Assign y according to the following rule: 
    Middle of 0s surrounded on left and right by 1s.

    Args:
    ----
        N: number of points

    Returns:
    -------
        Graph with assigned y values

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N):
    """Assign y according to the following rule: 
    Chess-like grid is created from 1s and 0s.

    Args:
    ----
        N: number of points

    Returns:
    -------
        Graph with assigned y values

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 and x_2 > 0.5 or x_1 > 0.5 and x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N):
    """Assign y according to the following rule: 
    Two circles are crated (0s surrounded by circle of 1s).

    Args:
    ----
        N: number of points

    Returns:
    -------
        Graph with assigned y values

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = x_1 - 0.5, x_2 - 0.5
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N):
    """Assign y according to the following rule: 
    Two not intersecting spirals are created - one with 1 class and one with 2 class.

    Args:
    ----
        N: number of points

    Returns:
    -------
        Graph with assigned y values

    """
    def x(t):
        return t * math.cos(t) / 20.0

    def y(t):
        return t * math.sin(t) / 20.0
    X = [(x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N //
        2))) + 0.5) for i in range(5 + 0, 5 + N // 2)]
    X = X + [(y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) /
        (N // 2))) + 0.5) for i in range(5 + 0, 5 + N // 2)]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {'Simple': simple, 'Diag': diag, 'Split': split, 'Xor': xor,
    'Circle': circle, 'Spiral': spiral}
