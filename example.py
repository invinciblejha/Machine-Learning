from machine_learning.prototypes.enn import enn
from machine_learning.prototypes.cnn import cnn


if __name__ == '__main__':
    training = [[1,1,1],[2,2,1],[3,3,1], [9,9,1],[10,10,10],[11,11,10],[15,15,10], [19,19,10], [20,20,20], [21,21,20]]
    print training
    print enn(training)
    print cnn(training)
