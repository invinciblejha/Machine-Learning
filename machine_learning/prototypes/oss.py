import math

import machine_learning.classifiers.knn as knn
from machine_learning.distance.euclidian_distance import euclidian_distance
from machine_learning.prototypes.cnn import cnn_for_unbalanced_datasets
from machine_learning.prototypes.tomek_links import tomek_links_for_unbalanced_datasets

def oss(training, dist = euclidian_distance):

    classes = list(set([t[-1] for t in training]))

    min_class = classes[0]
    for c in min_class:
        if classes.count(c) < min_class:
            min_class = c

    prototypes = cnn_for_unbalanced_datasets(training, min_class = min_class)
    prototypes = tomek_links_for_unbalanced_datasets(prototypes, min_class = min_class)

    return prototypes
            

