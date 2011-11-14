from machine_learning.prototypes.enn import enn
from machine_learning.prototypes.cnn import cnn
from machine_learning.prototypes.tomek_links import tomek_links
from machine_learning.prototypes.


if __name__ == '__main__':
    training = load_database('artificial_databases/a_database.data', separator = ',')

    results = []    
    results.append(enn(training))
    results.append(cnn(training))
    results.append(tomek_links(training))
    
    print tomek_links(training)
    database = load_database(file_name, separator)
