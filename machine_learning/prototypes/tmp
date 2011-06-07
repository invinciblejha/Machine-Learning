# encoding: utf-8
import numpy as np
import utils as utils
import pca as hama
import knn


def update_group_representant(group):
	'''
	Update a group when any instance is removed or
	added to the group. This function calculate the
	new prototype and update the group.
	group = (group_class, representant, group_instances)
	'''
	instances = group[2]
	
	mn = np.mean(np.asarray(instances)[:,:-1], axis = 0)
	mn = mn.tolist() + [group[0]]
	group[1] = mn


def generate_initial_groups(training):
	'''
	O grupo é representado por uma tupla
	(CLASSE, REPRESENTANTE, INSTANCIAS DO GRUPO)
	'''
	groups = []
	classes = [instance[-1] for instance in training]
	uniq_classes = set(classes)
	
	for c in uniq_classes:
		instances_c = filter(lambda instance: instance[-1] == c, training)
		to_mean = np.asarray([i[:-1] for i in instances_c])
		mn = np.mean(to_mean, axis = 0)
		mn = mn.tolist() + [c]
		groups.append([c , mn, instances_c])

	return groups

def calc_nearest_representing(groups):
	contador_de_saida = 0
	for group in groups:
		elements_for_new_group = []
		
		representants = [g[1] for g in groups]

		actual_representing = group[1]	#obtem o representante do grupo
		instances = group[2]		#obtem as instancias que pertencem ao grupo
		
		inst_orig_nearests = []
		diff_count = 0

		for sample in instances:
			[nearest] = knn.get_knn(1, sample, representants)
			tupla = (sample, actual_representing, nearest)
			inst_orig_nearests.append(tupla)
			
			#print sample, actual_representing, nearest
			
			if nearest != actual_representing:
				diff_count = diff_count + 1

		
		# se todos os elementos do grupo possuirem como o prototipo mais proximo
		# o prototipo do grupo ao qual pertencem.
		if diff_count == 0:
			contador_de_saida = contador_de_saida + 1
		
		# se TODOS os elementos do grupo possuirem como o prototipo mais proximo
		# um prototipo representante de outro grupo.
		elif diff_count == len(inst_orig_nearests):
			elements = [e[0] for e in inst_orig_nearests]
			P, med = hama.pca([e[:-1] for e in elements], 1)
			normal_vector = P
			prototipo = group[1][:-1]

			[d] = hama.proj(P, prototipo, med)
			
			for sample in instances:
				[di] = hama.proj(P, sample[:-1], med)
				if -d < di:
					elements_for_new_group.append(sample)
					group[2].remove(sample)

		# se ALGUM dos elementos do grupo possuirem como prototipo mais proximo
		# um prototipo representante de outro grupo.
		elif diff_count > 0:
			# a tupla e formada por (AMOSTRA, ATUAL_REPRESENTANTE, REPRESENTANTE_MAIS_PROXIMO)
			for tupla in inst_orig_nearests:

				# se o atual representante for o mais proximo
				# if tupla[1] == tupla[2]:
				#	print ''					
	
				# se a classe do prototipo atual é diferente da classe do protótipo mais próximo
				# mais proximo.
				# elif tupla[1][-1] != tupla[2][-1]:
				if tupla[1][-1] != tupla[2][-1]:
					group[2].remove(tupla[0])
					elements_for_new_group.append(tupla[0])
				# se forem de classes iguais
				else:
					nearest_index = -1
					for i in range(len(groups)):
						if groups[i][1] == tupla[2]:
							nearest_index = i
					
					groups[nearest_index][2].append(tupla[0])
					group[2].remove(tupla[0])
		
						
		if len(elements_for_new_group) > 0:	
			[ng] = generate_initial_groups(elements_for_new_group)
			groups.append(ng)

		for g in groups:
			update_group_representant(g)

	if contador_de_saida != len(groups):
		return calc_nearest_representing(groups)
	
	return groups


def sgp(training):
	groups = generate_initial_groups(training)
	groups = calc_nearest_representing(groups)
	return [group[1] for group in groups]	

if __name__ == '__main__':
	training = [[1,1,1],[2,2,1],[3,3,1],[10,10,10],[11,11,10],[12,12,10], [200,200,100], [100,102,1]]
	
	print '-------------------------------------------------------------------------'
	groups = generate_initial_groups(training)
	for g in groups:
		print g
	print '------------------------- after algorithm--------------------------------'
	new_groups =  calc_nearest_representing(groups)
	for g in new_groups:
		print g
	print '-------------------------------------------------------------------------'




