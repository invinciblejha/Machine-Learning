from machine_learning.classifiers.knn import *
from machine_learning.distance.euclidian_distance import *

def get_acertion_tax(k, test_list, training_list, range_vector, dist = euclidian_distance):
	right = 0
	for test_sample in test_list:
		nearest = get_knn(k, test_sample, training_list, dist, range_vector)
		knn_result = get_knn_result(nearest)
		if knn_result == test_sample[-1]:
			right = right + 1

	return 100*float(right)/float(len(test_list))
