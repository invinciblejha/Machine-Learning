import numpy as np

class Group:

	def __init__(self, instances = [], representant = [], classe = None, update = False):
		self.instances = instances
		if update == True:
			self.update_representant()
			self.update_classe()
		else:
			self.representant = representant
			self.classe = classe


	def add_instance(self, instance, update = False):
		self.instances.append(instance)
		if update == True:
			self.update_representant()

	def remove_instance(self, instance, update = False):
		self.instances.remove(instance)
		if update == True:
			self.update_representant()

	def update_representant(self):
		mn = np.mean(np.asarray(self.instances)[:,:-1], axis = 0)
		mn = mn.tolist() + [self.classe]

	def update_classe(self):
		self.classe = self.get_representant()[-1]

	def update_all(self):
		self.update_classe()
		self.update_representant()

	def get_classe(self):
		return self.classe

	def get_representant(self):
		return self.representant

	def get_instances(self):
		return self.instances

	def count_instances():
		return len(self.instances)

	def is_empty():
		return self.count_instances() == 0
