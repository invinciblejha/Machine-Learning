import math


def is_unknown(att):
	return att == '?'


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


def hamming_distance(a, b):
	'''
	Returns the hamming distance of two vectors with categorical data.
	'''
	return sum(hamming_distance_i(ai, bi) for ai,bi in zip(a,b))

def hamming_distace_i(ai,bi):
	return (0 if ai == bi else 1)

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


def vdm_discretized(a, b, training):
	pass #TODO

def vdm_interpolad(a, b, training):
	pass #TODO

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


def hvdm(a, b, data_range = [], data_nature = []):
	pass #TODO


def dvdm(a, b, data_range = [], data_nature = []):
	pass #TODO


def ivdm(a, b, data_range = [], data_nature = []):
	pass #TODO

