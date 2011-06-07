import random
from machine_learning.utils.utils import get_transposte
from machine_learning.utils.utils import get_media
from machine_learning.utils.utils import get_variance

def generate_prototypes(matrix, qtd_c = 5):
	prototypes = []
	classes = list(set([line[-1] for line in matrix]))

	for c in classes:
		instances = filter(lambda inst: inst[-1] == c, matrix)
		atts = get_transposte(instances)[:-1]
		m_atts = [get_media(att) for att in atts]
		v_atts = [get_variance(att) for att in atts]

		#csts = [-0.5, -0.3,  0, 0.3, 0.5]
		for i in range(qtd_c):			
			prototype = [m + random.triangular(-0.7, 0.7, (float(i)/10) - 0.25)*v for m,v in zip(m_atts, v_atts)] + [c]
			prototypes.append(prototype)

	return prototypes

