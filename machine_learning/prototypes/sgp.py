import numpy as np
import machine_learning.classifiers.knn as knn
from machine_learning.utils.utils import *
import machine_learning.feat_analysis.pca as hama
from Group import Group

def generate_initial_groups(training):
	groups = []

	classes = [instance[-1] for instance in training]
	uniq_classes = set(classes)

	for c in uniq_classes:
		instances_c = filter(lambda inst: inst[-1] == c, training)
		g = Group(instances_c, update = True)
		groups.append(g)

	return groups

def get_all_representants(groups):
	return [g.get_representant() for g in groups]

def update_all_groups(groups):
	for g in groups:
		if g.is_empty():
			groups.remove(g)
		else:
			g.update_all()

def alg(groups):
	exit_count = 0
	for group in groups:

		all_representants = get_all_representants(groups)
	
		instance_and_nearest = []
		new_group = Group()
	
		for sample in group.get_instances():
			[nearest_rep] = knn.get_knn(1, sample, all_representants)

			if nearest_rep != group.get_representant():
				instance_and_nearest.append((sample, nearest_rep))
				
		if len(instance_and_nearest) == 0:
			exit_count = exit_count + 1

		elif len(instance_and_nearest) == group.count_instances():
			elements = group.get_instances()
			P, med = hama.pca([e[:-1] for e in elements], 1)
			normal_vector = P
			prototype = group.get_representant()[:-1]
			[d] = hama.proj(P, prototype, med)
			
			for inst in group.get_instances():
				[di] = hama.proj(P, inst[:-1], med)
				if -d < di:
					group.remove_instance(inst)
					new_group.add_instance(inst)
		else:
			for tupla in instance_and_nearest:
				bad_instance = tupla[0]
				nearest_representant = tupla[1]
				
				if nearest_representant != group.get_representant() and nearest_representant[-1] != group.get_classe():
					group.remove_instance(bad_instance)
					new_group.add_instance(bad_instance)
				elif nearest_representant != group.get_representant():
					group_index = -1
					[to_add] = filter(lambda g: g.get_representant() == nearest_representant, groups)
					to_add.add_instance(bad_instance)
					group.remove_instance(bad_instance)

		if not new_group.is_empty():
			new_group.update_all()
			groups.append(new_group)

		update_all_groups(groups)

	if exit_count != len(groups):
		return alg(groups)
		
	return groups
			
def sgp(training):
	groups = generate_initial_groups(training)
	groups = alg(groups)
	return [g.get_representant() for g in groups]
	
	
