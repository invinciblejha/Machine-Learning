
import numpy as np
import math

def euclidian_distance (a, b, r = None):
    return math.sqrt(((np.asarray(a) - np.asarray(b)) ** 2).sum())

