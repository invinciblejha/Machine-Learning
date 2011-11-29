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

    for i in [5,10]:
        for j in [0,1,5,10,15]:
            training = load_database('artificial_databases/' + str(i) + '_' + str(j) +  '_database.data', separator = ',')

            results = []    

            enn_prototype = training
            results.append(enn(training))
           
            results.append(cnn(training))
            results.append(tomek_links(training))
            results.append(oss(training))

            prototypes = generate_prototypes(training)
            results.append(lvq1(training, prototypes))
            results.append(lvq2(training, prototypes))
            results.append(lvq3(training, prototypes))

            results.append(sgp(training))
            results.append(sgp2(training))

            for result in results:
                print len(results)
                plt.plot(result)



