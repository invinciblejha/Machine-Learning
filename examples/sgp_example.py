import sys

from machine_learning.prototypes.sgp import sgp
from machine_learning.utils.evaluate import get_acertion_tax
from machine_learning.utils.database_loader import load_database

if __name__ == '__main__':
	test = load_database('databases/'+ sys.argv[2] + '.test')
	training = load_database('databases/'+ sys.argv[2] + '.train')
	
	prototypes = sgp(training)
	print prototypes

	print 'tamanho da base original %d' % (len(training))
	print 'tamanho da base pos-sqp  %d' % (len(prototypes))

	print 'taxa de acerto'
	print get_acertion_tax(1, test, prototypes)





