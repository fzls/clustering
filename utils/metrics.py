#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from functools import reduce, lru_cache
from algorithms.cluster import Cluster


def fixup(item:tuple):
    # item should be like ( 1, (2,3))
    if len(item) < 2 or type(item[1]) is not tuple:
        # if item is like (1) or (1, 2) or (1, 2, 3, ..., n)
        return (-1, item)
    return item
    pass


@lru_cache()
def distance(lhs: tuple, rhs: tuple) -> float:
    """
    返回两个数据点之间的距离
    :param lhs: item is like (1, (1,2,3,4)) (index, item)
    :param rhs:
    :return:
    """
    dim = len(rhs)
    _lhs = fixup(lhs)
    _rhs = fixup(rhs)

    return math.sqrt(sum([(_lhs[Cluster.VALUE][d] - _rhs[Cluster.VALUE][d]) ** 2 for d in range(dim)]))


def distance_cluster(c1, c2):
    return [distance(c1[i], c2[j]) for i in range(len(c1)) for j in range(len(c2))]


def odd(num):
    return num & 1


def even(num):
    return not odd(num)


def _centroid(c1, c2):
    data = distance_cluster(c1, c2)
    n = len(data)
    mid = n // 2
    _data = sorted(data)
    return _data[mid] if odd(n) else (_data[mid - 1] + _data[mid]) / 2


def avg_of_items(items):
    dim = len(items[0][Cluster.VALUE])
    return tuple(reduce(lambda s, item: s + item[Cluster.VALUE][i], items, 0) / len(items) for i in range(dim))

def ssd(items):
    """sum-of-squared-difference"""
    avg = avg_of_items(items)
    return sum([distance(item, (-1, avg)) ** 2 for item in items])


def _ward(c1, c2):
    # print(ssd(c1), ssd(c2), ssd(c1 + c2))
    return ssd(c1 + c2) - (ssd(c1) + ssd(c2))


def _avg(c1, c2):
    r = distance_cluster(c1, c2)
    return sum(r) / len(r)


def _min(c1, c2):
    r = distance_cluster(c1, c2)
    return min(r)


def _max(c1, c2):
    r = distance_cluster(c1, c2)
    return max(r)


def _energy_distance(c1, c2):
    return 2 * _avg(c1, c2) - _avg(c1, c1) - _avg(c2, c2)
