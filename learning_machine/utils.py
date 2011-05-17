import math

def get_media(l, key = float):
	return sum([key(e) for e in l])/len(l)

def get_variance(l, key = float):
	media = get_media(l, key = key)
	return math.sqrt(sum([(key(e) - media)**2 for e in l])/(len(l) - 1))

def get_normalized_vector(l):
	return map(lambda e: float(e)/(max(l) - min(l)), l)

def vector_operation(va, vb, operation = lambda a , b: a - b):
	while len(va) < len(vb): va.append(0)
	while len(vb) < len(va): vb.append(0)
	return [operation(va[i],vb[i]) for i in range(len(va))]

def get_range_vector(matrix):
	t_matrix = get_transposte(matrix)
	return [float(max(c)) - float(min(c)) for c in t_matrix]

def get_transposte(matrix):
	b = []
	for i in range((len(matrix[0]))):
		b.append([c for c in [l[i] for l in matrix]])
	return b

def calc_constants(t_training, categories):
	constants = []
	for i in range(len(t_training) - 1):
		column = t_training[i]
		column_types = list(set(column))
		for c_type in column_types:
			valor = column.count(c_type)
			chave = '|' + str(i) + ',' + str(c_type) + '|'
			constants.append((chave, valor))
			
		z = zip(t_training[-1], t_training[i])
		for category in categories:
			for c_type in column_types:
				valor = z.count((category, c_type))
				chave = '|' + str(i) + ',' + str(c_type) + ',' + str(category) + '|'
				constants.append((chave,valor))
	return constants

