from machine_learning.prototypes.sgp import sgp
from machine_learning.utils.evaluate import get_acertion_tax
from machine_learning.utils.database_loader import load_database
import sys

if __name__ == '__main__':

	database = 'glass'	
	if len(sys.argv) > 1:
		database = sys.argv[2]

	test = load_database('databases/'+ database + '.test')
	training = load_database('databases/'+ database + '.train')
	
	prototypes = sgp(training)

	print 'tamanho da base original %d' % (len(training))
	print 'tamanho da base pos-sqp  %d' % (len(prototypes))

	print 'taxa de acerto'
	print get_acertion_tax(1, test, prototypes)





