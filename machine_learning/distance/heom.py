import math
from euclidian_distance import euclidian_distance
from hamming_distance import hamming_distance


def heom(a, b, data_range = [], data_nature = []):
	'''
	Heterogeneous Euclidian-Overlap Metric

	Vector distance for heterogeneous data.
	HEOM uses euclidian distance for numerical data
	and hamming distance for categorical data.

	function parameters:
		a - vector to compare
		b - vector to compare
		data_nature - the data nature of the attributes of de vectors to be compared
			      it is 'n' for numerical and 'c' for categorical.
			      if not specified it will assume that the numerical is the official measure

	'''

	if len(data_range) == 0:
		data_range = [1 for i in range(len(a))]
	if len(data_nature) == 0:
		data_nature = ['n' for i in range(len(a))]
	
	heom_i_list = [heom_i(ai, bi, r, n) for ai, bi, r, n in zip(a, b, data_range, data_nature)]
	return math.sqrt(sum(heom_i_list))
	
	
def heom_i(ai, bi, att_range, nature):
	'''
	Returns the HEOM of one single atribute.
	'''
	if is_unknown(ai) and is_unknown(bi):
		return 0
	elif is_unknown(ai) or is_unknown(bi):
		return 1

	if nature == 'c':
		return hamming_distance_i(ai, bi)		
	elif nature == 'n':
		return euclidian_distance_i(float(ai), float(bi), att_range)

	return 0

