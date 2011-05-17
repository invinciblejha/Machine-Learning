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

NOT TESTED
'''
def vdm(a, b, training):
	return math.sqrt(sum([vdm_i(i, ai, bi) for i, ai, bi in zip(range(len(a)),a,b)]))

'''
NOT TESTED

'''
def vdm_i(i, ai, bi, training, q = 2):
	classes = set([e[-1] for e in training])
	
	ai_count_class = [len(filter(lambda e: e[i] == ai and e[-1] == c, training)) for c in classes]
	bi_count_class = [len(filter(lambda e: e[i] == bi and e[-1] == c, training)) for c in classes]

	n_ac = sum(ai_count_class)
	n_bc = sum(bi_count_class)
		
	vdmi = 0
	for za, zb in zip(ai_count_class, bi_count_class):
		diff = float(za)/n_ac - float(zb)/n_bc
		vdmi = vdmi + (abs(diff)**q)

	return vdmi



