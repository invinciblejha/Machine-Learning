import math
from machine_learning.classifiers.knn import get_knn
from machine_learning.classifiers.knn import get_knn_result
from machine_learning.distance.euclidian_distance import euclidian_distance

def enn(training, k = 3, weight = False, dist = euclidian_distance, range_vector = None):
    """
    Edited Nearest Neighbor

    """
    #TODO need to treat if weight == True
    markeds = []
    for sample in training:
        nearests = get_knn(k+1, sample, training, dist)
        result = get_knn_result(nearests[1:])
        if result != sample[-1]:
            markeds.append(sample)

    return filter(lambda e: not e in markeds, training)

