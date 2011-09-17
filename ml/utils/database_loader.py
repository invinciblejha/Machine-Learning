import numpy as np




def load_database(filename, separator = None, dtype = None):
    if separator == None:
        separator = "\t"

    all_labels = np.loadtxt(filename, delimiter = separator)
    return all_labels
