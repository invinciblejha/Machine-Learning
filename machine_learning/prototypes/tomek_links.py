import math
import random

import machine_learning.classifiers.knn as knn
from machine_learning.distance.euclidian_distance import euclidian_distance


def tomek_links(training, dist = euclidian_distance):
    links = []
    for t in training:
        nears = knn.get_knn(2, t, training, dist)
        near = nears[1]
        if t[-1] != near[-1]:
            links.append((t, near))

    prototypes = list(training)
    for (t, near) in links:
        if (near, t) in links:
            if t in prototypes:
                prototypes.remove(t)
            if near in prototypes:
                prototypes.remove(near)

    return prototypes
            

