import utils
from knn import get_knn
from knn import get_knn_result
from utils import euclidian_distance

def load_list(string, separator = "\t"):
	try:
		f = open(string, "r")
		s = list(set([line for line in f]))
		f.close()
	except:
		s = []
	
	l_tmp = [v.strip().split(separator) for v in s]
	l_floats = [[float(e) for e in v[:-1]] + [v[-1]] for v in l_tmp]
	return l_floats


def get_acertion_tax(k, test_list, training_list, range_vector, dist = euclidian_distance):
	right = 0
	for test_sample in test_list:
		nearest = get_knn(k, test_sample, training_list, dist, range_vector)
		knn_result = get_knn_result(nearest)
		if knn_result == test_sample[-1]:
			right = right + 1

	return 100*float(right)/float(len(test_list))
