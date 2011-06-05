import math

def hamming_distance(a, b):
	'''
	Returns the hamming distance of two vectors with categorical data.
	'''
	return sum(hamming_distance_i(ai, bi) for ai,bi in zip(a,b))

def hamming_distace_i(ai,bi):
	return (0 if ai == bi else 1)

