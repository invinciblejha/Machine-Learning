import math


def vdm(a, b, training):
	'''
	Returns the vdm distance of two vectors with categorical data.
	The VDM (Value Difference Metric) finds out when two values have the same
	distribution over some class.

	Is usually better than Hamming Distance.

	NOT TESTED
	'''
	return math.sqrt(sum([vdm_i(i, ai, bi) for i, ai, bi in zip(range(len(a)),a,b)]))



def vdm_i(i, ai, bi, training, q = 2):
	'''
	Returns the vdm distance of a single atribute.
	
	NOT TESTED
	'''
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

