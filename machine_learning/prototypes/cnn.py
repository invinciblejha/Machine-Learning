import math
import random

from machine_learning.classifiers.knn import get_knn
from machine_learning.distance.euclidian_distance import euclidian_distance


def cnn (training, dist = euclidian_distance, range_vector = None):

    prototypes = []

    for c in set([t[-1] for t in training]):
        inst = random.choice(filter(lambda inst: inst[-1] == c, training))
        prototypes.append(inst)


    for t in training:
        nearest = get_knn(1, t, prototypes, dist)
        if t[-1] != nearest[0][-1]:
            prototypes.append(t)

    return prototypes        
        
def cnn_for_unbalanced_datasets(training, dist = euclidian_distance, range_vector = None, min_class = None):
    prototypes = []

    if min_class != None:
        prototypes = filter(lambda inst: inst[-1] == min_class, training)

    classes = set([t[-1] for t in training])
    classes.remove(min_class)

    for c in classes: 
        inst = random.choice(filter(lambda inst: inst[-1] == c, training))
        prototypes.append(inst)
 
    for t in training:
        nearest = get_knn(1, t, prototypes, dist)
        if t[-1] != nearest[0][-1]:
            prototypes.append(t)
    
    return prototypes 
    
    
    

    
