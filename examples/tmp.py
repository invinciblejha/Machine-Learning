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
    training = load_database('artificial_databases/a_database.data', separator = ',')
    results = []
    s2 = sgp(training)
    results.append((s2, len(s2)))

    for result in results:
        print result[1]
        plt.plot(result[0])
        a = raw_input('next?')



