import numpy as np

class Group:

	def __init__(self, instances = None, representant = [], classe = None, update = False):
		
		self.instances = instances if instances else []
		self.representant = representant if representant else []
		self.classe = classe if classe else None

		if update == True:
			self.update_representant()
			self.update_classe()


	def __add__(self, other):
		r = Group()
		r.instances = self.get_instances() + other.get_instances()
		r.update_all()
		return r

	def add_instance(self, instance, update = False):
		self.instances.append(instance)
		if update == True:
			self.update_representant()

	def remove_instance(self, instance, update = False):
		self.instances.remove(instance)
		if update == True:
			self.update_representant()

	def update_representant(self):
		ar = np.asarray(self.instances)[:,:-1]
		ar = ar.astype(float)
		mn = np.mean(ar, axis = 0)
		c = (self.classe if self.classe != None else self.instances[0][-1])
		self.representant = mn.tolist() + [c]

	def update_classe(self):
		if self.get_representant():
			self.classe = self.get_representant()[-1]
		elif not self.is_empty():
			self.classe = self.get_instances()[0][-1]
		else:
			print 'ERROR update classe'

	def update_all(self):
		self.update_representant()
		self.update_classe()

	def get_classe(self):
		return self.classe

	def get_representant(self):
		return self.representant

	def get_instances(self):
		return self.instances

	def count_instances(self):
		return len(self.instances)

	def is_empty(self):
		return self.count_instances() == 0



