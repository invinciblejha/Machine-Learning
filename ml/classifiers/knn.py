
from ml.distances.numerical import euclidian_distance


def knn_result (k, sample, train_data, train_class, weight = False):

    insts, classes, dists = get_knn_infos(k, sample, train_data, train_class)

    if weight == False:
        return max(set(classes)


def get_knn_infos (k, sample, train_data, train_class):

    instance_distance = []
    for instance, instance_class in zip(train_data, train_class):
        distance = euclidian_distance(sample, instance)
        distances.append((instance, instance_class, distance))

    distances.sort(key = lambda e: e[-1])
    return distances[:k]
