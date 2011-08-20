# coding: utf-8

def hamming_distance (a, b):
    '''
    
    '''
    hm_dist_i = lambda ai, bi: (0 if ai == bi else 1)
    dists = map(hm_dist_i, a, b)
    return sum(dists)
