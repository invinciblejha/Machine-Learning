from machine_learning.utils.database_loader import load_database

from machine_learning.prototypes.enn import enn
from machine_learning.prototypes.cnn import cnn
from machine_learning.prototypes.tomek_links import tomek_links
from machine_learning.prototypes.oss import oss
from machine_learning.prototypes.gaussian import generate_prototypes
from machine_learning.prototypes.lvq import lvq1
from machine_learning.prototypes.lvq import lvq2
from machine_learning.prototypes.lvq import lvq3
from machine_learning.prototypes.sgp import sgp
from machine_learning.prototypes.sgp import sgp2

import plot as plt

if __name__ == '__main__':
    training = load_database('artificial_databases/c_database.data', separator = ',')

    results = []    

    results.append(enn(training))
    print '1'
    results.append(cnn(training))
    print '2'
    results.append(tomek_links(training))
    print '3'
    results.append(oss(training))
    print '4'

    prototypes = generate_prototypes(training)
    print '5'
    results.append(lvq1(training, prototypes))
    print '6'
    results.append(lvq2(training, prototypes))
    print '7'
    results.append(lvq3(training, prototypes))
    print '8'

    results.append(sgp(training))
    print '9'
    results.append(sgp2(training))
    print '10'

    for result in results:
        plt.plot(result)



