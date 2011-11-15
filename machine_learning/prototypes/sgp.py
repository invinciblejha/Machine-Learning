# coding: utf-8

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

def get_group_by_representant(representant, groups):
	gs = filter(lambda g: g.get_representant() == representant, groups)
	group = gs[0]
	return group

def alg(groups):
	exit_count = 0
	for group in groups:

		all_representants = get_all_representants(groups)
	
		instance_and_nearest = []
		new_group = Group()
	
		for sample in group.get_instances():
			[n1,n2] = knn.get_knn(2, sample, all_representants)

			nearest_rep = n1
			if n1[:-1] == n2[:-1]:
				if sample[-1] == n2[-1]:
					nearest_rep = n2

			if nearest_rep != group.get_representant():
				nearest_g = get_group_by_representant(nearest_rep, groups)
				instance_and_nearest.append((sample, nearest_g))
				
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
				if d < di:
					group.remove_instance(inst)
					new_group.add_instance(inst)
		else:
			for tupla in instance_and_nearest:
				bad_instance = tupla[0]
				nearest_g = tupla[1]
				
				# [new_nearest] = knn.get_knn(1, bad_instance, [nearest_g.get_representant(), group.get_representant()])
				# if new_nearest == nearest_g.get_representant():
				if nearest_g.get_representant() != group.get_representant() and nearest_g.get_classe() != group.get_classe():
					group.remove_instance(bad_instance)
					new_group.add_instance(bad_instance)
				elif nearest_g.get_representant() != group.get_representant(): # mas são da mesma classe
					nearest_g.add_instance(bad_instance)
					group.remove_instance(bad_instance)
				#	nearest_g.update_all()
				#	group.update_all()

		if not new_group.is_empty():
			new_group.update_all()
			groups.append(new_group)

		update_all_groups(groups)

	if exit_count != len(groups):
		return alg(groups)
		
	return groups

def merging_step(groups):
	representants = get_all_representants(groups)
	for group in groups:
		merge = True
		snd_nearest_group = None
		for pattern in group.get_instances():
			nearests = knn.get_knn(2, pattern, representants)
			snd_tmp = get_group_by_representant(nearests[1], groups)
			if snd_nearest_group == None:
				snd_nearest_group = snd_tmp
				if snd_nearest_group.get_classe() != group.get_classe():
					merge = False
					break
			elif snd_tmp != snd_nearest_group:
				merge = False
				break
		
		if merge == True and snd_nearest_group != None:
			new_group = snd_nearest_group + group
			groups.remove(group)
			groups.remove(snd_nearest_group)
			groups.append(new_group)
			
			merging_step(groups) # RECURSSION
			return True
	return False	

def prunning_step(groups, r_min = 0.1, r_mis = 0.1):
	to_remove = []
	max_group_len = float(len(max(groups, key = len)))
	for group in groups:
		if len(group)/max_group_len < r_min:
			to_remove.append(group)
	
	for group in to_remove:
		groups.remove(group)

	return len(to_remove) > 0
			
def sgp(training):
	groups = generate_initial_groups(training)
	groups = alg(groups)
	# merging_step(groups)
	return [g.get_representant() for g in groups]
	

def sgp2(training, r_min = 0.1, r_mis = 0.1):
	groups = generate_initial_groups(training)
	groups = alg(groups)
	merging_step(groups)
	prunning_step(groups, r_min, r_mis)	#TODO parte que usa o RMIS
	return [g.get_representant() for g in groups]
	



