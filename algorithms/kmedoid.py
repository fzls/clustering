#!/usr/bin/env python
# -*- coding: utf-8 -*-
from algorithms.kmeans import KMeans
from utils.log import log

class KMedoid(KMeans):
    def __init__(self, n_clusters: int, max_iter=100, init='k-means++', n_init=10, tol=0.0001):
        super().__init__(n_clusters, max_iter, init, n_init, tol)

    def get_new_center(self, cluster: list) -> tuple:
        """获取新的聚类中心（通过取聚类中各数据的中位数）"""
        means = [self.mean(m, cluster) for m in cluster]

        medoid = min(cluster, key=lambda m: self.mean(m, cluster))

        log.debug("\ncluster: %s\nmeans: %s\nmedoid: %s"%(cluster, means, medoid))

        return medoid

    def mean(self, m, cluster):
        from utils import metrics
        from functools import reduce

        return reduce(lambda s,item: s+metrics.distance(item, m), cluster, 0.0) / len(cluster)



if __name__ == '__main__':
    from utils.functions import test_dummy_data,test_iris

    test_iris(KMedoid(3))