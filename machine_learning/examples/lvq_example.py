import sys
import getopt
from machine_learning.aux import load_list
from aux import get_acertion_tax 
from knn import get_knn
from distance import euclidian_distance
from utils import get_range_vector
from prototypes.lvq_utils import generate_prototypes
from prototypes.lvq import lvq1
from prototypes.lvq import lvq2
from prototypes.lvq import lvq3

if __name__ == '__main__':
	print " K	KNN	LVQ1	LVQ2	LVQ3\n"
	
	args =  sys.argv
	optlist, args = getopt.getopt(sys.argv[1:],'d:a:w:e:l:', ['generate-prototypes','help'])
	optlist = dict(optlist)

	if optlist.has_key('--help'):
		print 'help, I need somebody, help, not just anybody, help'
		exit(0)

	database = optlist.get('-d')
	alpha = float(optlist.get('-a'))
	window = float(optlist.get('-w'))
	epsilon = float(optlist.get('-e')) 
	limit = float(optlist.get('-l'))

	training = load_list(database + "/treinamento")
	test = load_list(database + "/teste")
	
	range_vector = get_range_vector([e[:-1] for e in training])

	prototypes = []
	if not optlist.has_key('--generate-prototypes'):
		prototypes = load_list(database + '/prototypes')
	
	if (len(prototypes) == 0):
		prototypes = generate_prototypes(training)
		f = open(database+'/prototypes','w')
		for e in prototypes:
			for a in e:
				f.write(str(a) + '\t')
			f.write('\n')
		f.close()
			

	lvq1_training = lvq1(training, prototypes, range_vector, limit, alpha)
	lvq2_training = lvq2(training, prototypes, range_vector, limit, alpha, window)
	lvq3_training = lvq3(training, prototypes, range_vector, limit, alpha, window, epsilon)

	for k in [1, 3, 5]:
		knn_tax = get_acertion_tax(k, test, prototypes, range_vector)
		lvq1_tax = get_acertion_tax(k, test, lvq1_training, range_vector)
		lvq2_tax = get_acertion_tax(k, test, lvq2_training, range_vector)
		lvq3_tax = get_acertion_tax(k, test, lvq3_training, range_vector)
		print "%2d	%.3f	%.3f	%.3f	%.3f\n" % (k, knn_tax, lvq1_tax, lvq2_tax, lvq3_tax)

		


