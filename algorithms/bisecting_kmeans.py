#!/usr/bin/env python
# -*- coding: utf-8 -*-
from algorithms.cluster import Cluster
from utils.log import log

class BisectingKmeans(Cluster):
    def __init__(self, k):
        self.k = k

    def fit(self, items: list) -> list:
        clusters = [list(enumerate(items))]
        for t in range(1, self.k):
            cluster_index = self.choose_one_cluster_to_bisect(clusters)
            log.info('choose cluster %d to bisect at loop %d'%(cluster_index, t))
            clusters+= self.bisect(clusters.pop(cluster_index))
        return clusters
        pass

    def bisect(self, cluster):
        from algorithms.kmeans import KMeans
        res = KMeans(2).fit([item[Cluster.VALUE] for item in cluster])
        return [[cluster[i[Cluster.INDEX]] for i in t] for t in res]

    def choose_one_cluster_to_bisect(self, clusters):
        from utils import metrics
        return max(range(len(clusters)), key=lambda i: metrics.ssd(clusters[i]))
        pass

if __name__ == '__main__':
    from utils.functions import test_dummy_data, test_iris

    test_iris(BisectingKmeans(3))
