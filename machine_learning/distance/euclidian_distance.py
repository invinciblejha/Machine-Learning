import math

def euclidian_distance(a, b, data_range = []):
	'''
	Returns the euclidian distance of two vectors of numerical data.
	data_range can be defined using the function get_data_range.
	'''
	if data_range == []:
		data_range = [1 for i in range(len(a))]
	
	return sum([euclidian_distance_i(ai, bi, ri)**2 for ai, bi, ri in zip(a,b, data_range)])


def euclidian_distance_i(num_a, num_b, num_range = 1):
	'''
	Returns de euclidian distance of an atribute i.
	'''
	return abs((float(num_a) - float(num_b))/num_range)

