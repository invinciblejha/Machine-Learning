import math
from machine_learning.distance.euclidian_distance import euclidian_distance
from machine_learning.utils.utils import get_range_vector
from machine_learning.utils.utils import vector_operation

def get_knn(k, sample, training, dist = euclidian_distance, range_vector = []):
	nearest = []
	for training_instance in training:
		instance_dist = dist(training_instance[:-1], sample[:-1], range_vector)
		nearest.append(training_instance + [instance_dist])
	
	nearest.sort(key = lambda near: near[-1])
	return [near[:-1] for near in nearest[:k]]

def load_knn (k, sample, training, weight = False, dist = euclidian_distance, range_vector = None):
    nearests = []
    for instance in training:
        instance_dist = dist(instance[:-1], sample[:-1], range_vector)
        nearests.append((instance, instance_dist))
    
    nearests.sort(key = lambda near: near[-1])
    return map(lambda tup: tup[0], nearests)

def get_knn_indexs(k, sample, training, dist = euclidian_distance, range_vector = []):
	nearest = []
	for i in range(len(training)):
		instance_dist = dist(training[i][:-1], sample[:-1])
		nearest.append(training[i] + [instance_dist] + [i])
	nearest.sort(key = lambda near: near[-2])
	return [near[-1] for near in nearest[0:k]]

def get_knn_result(k_nearest):
	classes = [near[-1] for near in k_nearest]
	return max(set(classes), key = classes.count)
