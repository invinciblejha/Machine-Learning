import math

'''
function that takes de euclidian distance of an atribute i.
'''
def euclidian_distance_i(num_a, num_b, num_range = 1):
	return abs((float(num_a) - float(num_b))/num_range)

'''
function that takes the euclidian distance of two vectors of numerical data.
data_range can be defined using the function get_data_range.
'''
def euclidian_distance(a, b, data_range = []):
	if data_range == []:
		data_range = [1 for i in range(len(a))]
	return sum([euclidian_distance_i(ai, bi, ri)**2 for ai, bi, ri in zip(a,b, data_range)])


'''
function that takes the hamming distance of two vectors with categorical data.
'''
def hamming_distance(a, b):
	hamming_distance_i = lambda ai, bi: (0 if ai == bi else 1)
	return sum(hamming_distance_i(ai, bi) for ai,bi in zip(a,b))


'''
Function that takes the vdm distance of two vectors with categorical data.
The VDM (Value Difference Metric) finds out when two values have the same
distribution over some class.

Is usually better than Hamming Distance.
'''
def vdm(a, b):
	pass






