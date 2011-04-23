import math
from utils import euclidian_distance
from utils import get_range_vector
from utils import vector_operation

def get_knn(k, sample, training, dist = euclidian_distance, range_vector = []):
	nearest = []
	for training_instance in training:
		instance_dist = dist(training_instance[:-1], sample[:-1], range_vector)
		nearest.append(training_instance + [instance_dist])
	
	nearest.sort(key = lambda near: near[-1])
	return [near[:-1] for near in nearest[:k]]


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


