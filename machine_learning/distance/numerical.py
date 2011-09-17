# coding: utf-8

import numpy as np

def euclidian_distance(a, b, range_vector = None):
    """

    """
    if range_vector == None:
        range_vector = np.tile([1], len(a))

    return (map(lambda e: e ** 2, a - b) / range_vector).sum()

