from machine_learning.prototypes.sgp import sgp
from machine_learning.prototypes.sgp import generate_initial_groups
from machine_learning.prototypes.sgp import alg
from machine_learning.prototypes.sgp import merging_step
from machine_learning.prototypes.Group import Group
import random

if __name__ == '__main__':

	'''	
	training = []
	origin = 10
	for center in [(origin,origin), (origin,-origin), (-origin, -origin), (-origin, origin)]:
		for i in range(3):
			x = random.gauss(center[0], random.random())
			y = random.gauss(center[1], random.random())
			classe = int(center[0] != center[1])
			training.append([x,y, classe]) 
	'''	
	training = [[1,1],[2,1],[3,1],[4,2],[5,2],[6,2],[7,1],[8,1], [9,2],[10,2], [11,1],[12,1]] # LINE EXAMPLE
	groups = generate_initial_groups(training)
	groups = alg(groups)
	merged = merging_step(groups)

	for g in groups:
		print '------------------------------------------------------------------------------'
		print g.get_classe()
		print g.get_representant()
		print g.get_instances()
		print '------------------------------------------------------------------------------'
		
