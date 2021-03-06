# coding: utf-8
import numpy as np
import warnings

__author__ = "Adrien Guille"
__email__ = "adrien.guille@univ-lyon2.fr"


def erdem_correlation(array_1, array_2):
    a_12 = np.float64(0)
    a_1 = np.float64(0)
    a_2 = np.int64(0.)
    warnings.filterwarnings('ignore')

    for i in range(1, len(array_1)):
        a_12 += np.float64((array_1[i] - array_1[i-1]) * (array_2[i] - array_2[i-1]))
        a_1 += (array_1[i] - array_1[i-1]) * (array_1[i] - array_1[i-1])
        a_2 += (array_2[i] - array_2[i-1]) * (array_2[i] - array_2[i-1])
    if((len(array_1) - 1) <= 0):
        a_1 = 0
    elif(a_1/(len(array_1) - 1) < 0):
        a_1 = 0
    else:
        a_1 = np.sqrt(a_1/(len(array_1) - 1))
    if((len(array_2) - 1) <= 0):
        a_2 = 0
    elif(a_2/(len(array_2) - 1) < 0):
        a_2 = 0
    else:
        a_2 = np.sqrt(a_2/(len(array_2) - 1))
    if(len(array_1) * a_1 * a_2 == 0):
        coefficient = 0
    else:
        coefficient = a_12/(len(array_1) * a_1 * a_2)
    return coefficient


def overlap_coefficient(interval_0, interval_1):
    intersection_cardinality = float(min(interval_0[1], interval_1[1]) - max(interval_0[0], interval_1[0]))
    smallest_interval_cardinality = float(min(interval_0[1] - interval_0[0], interval_1[1] - interval_1[0]))
    if not smallest_interval_cardinality :
        smallest_interval_cardinality = 1
    return float(intersection_cardinality / smallest_interval_cardinality)
