from machine_learning.feat_analysis.pca import pca
from machine_learning.feat_analysis.pca import proj
from machine_learning.utils.evaluate import get_acertion_tax
from machine_learning.utils.database_loader import load_database
import numpy as np

if __name__ == '__main__':

	database = 'glass'	# the name of the database you want to run
	components = 3		# the number of components you want to use in PCA

	training = load_database('databases/' + database + '.train')
	test = load_database('databases/' + database + '.test')

	training_feats = [t[:-1] for t in training]
	training_class = [t[-1] for t in training]
	
	test_feats = [t[:-1] for t in test]
	test_class = [t[-1] for t in test]

	P, mn = pca(training_feats, components)
	
	pca_training = proj(P, training_feats, mn).tolist()
	pca_training = [a + [b] for (a,b) in zip(pca_training, training_class)]
	
	pca_test = proj(P, test_feats, mn).tolist()
	pca_test = [a + [b] for (a,b) in zip(pca_test, test_class)]

	print '\tK\tKNN\tPCA'
	for k in [1,3,5]:
		print '\t%d	%.2f	%.2f' % (k, get_acertion_tax(k, test, training), get_acertion_tax(k, pca_test, pca_training))

	
	
