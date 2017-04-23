#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import lru_cache

from algorithms.cluster import Cluster
from utils import metrics
from utils.log import log

class AgglomerativeClustering(Cluster):
    def __init__(self, k=3, linkage = 'average'):
        self.k = k
        # TODO: customize linkage
        self._linkage = linkage
        pass

    def fit(self, items: list) -> list:
        # TODO
        # 将原始数据集分为n个聚类
        clusters = [[indexed_items] for indexed_items in enumerate(items)]
        # 按照一定标准，每次将最相近的两个聚类合并，直到只剩k个聚类为止
        n = len(items) - self.k
        for i in range(n):
            c1_index, c2_index = self.find_nearest_two_clusters(clusters)
            self.merge_clusters(clusters, c1_index, c2_index)
            # self.print(clusters)
            print("\r%.2f%%"%(100*(i+1)/n), end='')
            if i == n-1:
                print()
        return clusters

    def find_nearest_two_clusters(self, clusters):
        return self._brute_force(clusters)

    def _brute_force(self, clusters):
        n = len(clusters)
        return min([(i, j) for i in range(n) for j in range(i + 1, n)],
                   key=lambda pair: self.linkage(tuple(clusters[pair[0]]), tuple(clusters[pair[1]])))

    @lru_cache(10000)
    def linkage(self, c1, c2):
        return metrics._avg(c1, c2)
        pass

    def merge_clusters(self, clusters, c1_index, c2_index):
        clusters[c1_index] += clusters.pop(c2_index)


if __name__ == '__main__':
    from utils.functions import test_dummy_data,test_iris

    test_iris(AgglomerativeClustering())
