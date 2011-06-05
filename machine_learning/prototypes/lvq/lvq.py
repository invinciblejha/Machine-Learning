import math
from knn import get_knn_indexs
from distance import euclidian_distance
from utils import vector_operation


def in_window(x, mi, mj, w):
	di = euclidian_distance(mi, x)
	dj = euclidian_distance(mj, x)
	s = (1 - w)/(1 + w)
	return min(di/dj, dj/di) > s


def lvq1_ajust(sample, prototype, alpha, epsilon = 1.0):
	op = lambda a, b: a - b

	prototype_category = prototype[-1]
	if sample[-1] == prototype[-1]:
		op = lambda a, b: a + b
	
	factor_1 = prototype[:-1]
	factor_2 = vector_operation(sample[:-1], prototype[:-1], lambda a,b: a - b)
	factor_2 = [epsilon*alpha*e for e in factor_2]
	new_prototype = vector_operation(factor_1,factor_2, op) + [prototype_category]
	return new_prototype

def lvq1(training, prototypes, range_vector = [], limit = 1000, alpha = 0.02):
	times = 0
	new_prototypes = [p for p in prototypes]
	while times < limit:
		sample = training[times%len(training)]
		knn_indexs = get_knn_indexs(1, sample, new_prototypes, euclidian_distance, range_vector)
		
		alpha_t = alpha * math.exp(-times/(limit/5))
		for i in knn_indexs:
			prototype = new_prototypes[i]
			new_prototypes[i] = lvq1_ajust(sample, prototype, alpha_t)
		times = times + 1	

	return new_prototypes


def lvq2(training, prototypes, range_vector = [], limit = 1000, alpha = 0.02, window = 0.70):	
	lvq1_prototypes = lvq1(training, prototypes, range_vector, limit)
	new_prototypes = lvq1_prototypes
	times = 0
	while times < limit:
		sample = training[times%len(training)]
		knn_indexs = get_knn_indexs(2, sample, new_prototypes, euclidian_distance, range_vector)
			
		mi = new_prototypes[knn_indexs[0]]
		mj = new_prototypes[knn_indexs[1]]

		alpha_t = alpha * math.exp(-times/(limit/5))
		if in_window(sample, mi, mj, window):
			if mi[-1] != mj[-1] and (mi[-1] == sample[-1] or mj[-1] == sample[-1]):
				new_prototypes[knn_indexs[0]] = lvq1_ajust(sample, mi, alpha_t)
				new_prototypes[knn_indexs[1]] = lvq1_ajust(sample, mj, alpha_t)
		times = times + 1
	
	return new_prototypes


def lvq3(training, prototypes, range_vector = [], limit = 1000, alpha = 0.02, window = 0.70, epsilon = 0.3):
	lvq1_prototypes = lvq1(training, prototypes, range_vector, limit)
	new_prototypes = lvq1_prototypes
	times = 0
	while times < limit:
		sample = training[times%len(training)]
		knn_indexs = get_knn_indexs(2, sample, new_prototypes, euclidian_distance, range_vector)
		mi = new_prototypes[knn_indexs[0]]
		mj = new_prototypes[knn_indexs[1]]

		alpha_t = alpha * math.exp(-times/(limit/5))

		if in_window(sample, mi, mj, window):
			if mi[-1] != mj[-1] and (mi[-1] == sample[-1] or mj[-1] == sample[-1]):
				new_prototypes[knn_indexs[0]] = lvq1_ajust(sample, mi, alpha_t)
				new_prototypes[knn_indexs[1]] = lvq1_ajust(sample, mj, alpha_t)
			if mi[-1] == sample[-1] and mj[-1] == sample[-1]:
				new_prototypes[knn_indexs[0]] = lvq1_ajust(sample, mi, alpha_t, epsilon)
				new_prototypes[knn_indexs[1]] = lvq1_ajust(sample, mj, alpha_t, epsilon)

		times = times + 1

	return new_prototypes





