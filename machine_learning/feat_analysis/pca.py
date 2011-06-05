# -*- coding: utf-8 -*-

import numpy as np

def pca(data, n):
    # Converte os dados em uma matrix
    data_mtx = np.asmatrix(data)

    # Calcula a media entre as amostras (linha)
    mn = np.mean(data_mtx, axis=0)

    # Centraliza os dados subitraindo da media
    c_data = data_mtx - np.tile(mn, (len(data_mtx), 1))

    # Calcula a matriz de covariancia dos dados
    # centralizados
    cov = np.cov(c_data, rowvar=0)

    # Calcula os auto-valores e auto-vetores da
    # matriz de covariancia
    D,V = np.linalg.eig(cov)

    # Ordena os indices de forma decrescente dos
    # auto-valores
    idx_desc = np.argsort(D)[::-1]

    # Seleciona a matriz de projecao com os n
    # maiores auto-vetores
    P = V[:,idx_desc[:n]]
    
    return P, mn


def proj(P, data, mn=None):
    data_mtx = np.asmatrix(data)
    
    if mn != None:
        c_data = data_mtx - np.tile(mn, (len(data_mtx), 1))
        data_proj = np.dot(P.T, c_data.T)
        return np.asarray(data_proj.T)
    else:
        data_proj = np.dot(P.T, data_mtx.T)
        return np.asarray(data_proj.T)
