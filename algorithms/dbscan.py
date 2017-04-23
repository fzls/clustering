#!/usr/bin/env python
# -*- coding: utf-8 -*-
from algorithms.cluster import Cluster
from utils.log import log

class DBSCAN(Cluster):
    def __init__(self, eps=0.5, min_samples=5):
        self.eps = eps
        self.min_samples = min_samples
        pass

    def fit(self, items: list):
        # 找到核心点
        core_indexes = []
        for item_index,item in enumerate(items):
            # 计算与该点距离为eps的点的个数
            cnt = len(self.items_within_eps(item, items))
            # 将密度高于给定阈值的加入核心点钟
            if cnt>=self.min_samples:
                core_indexes.append(item_index)

            log.debug(list(sorted(map(lambda i: self.distance(item, i), items))[:4]))
        # 将核心点eps范围内的点标记为其聚类内的点
        clusters = []
        cluster_label = -1
        labels = [-1]*len(items)
        for core_index in core_indexes:
            core = items[core_index]
            # 若该核心点未被标记过，则新建一个聚类，否则获得其聚类标号
            if labels[core_index] == -1:
                clusters.append([])
                cluster_label+=1
                label = cluster_label
            else:
                label = labels[core_index]

            # 将该核心点附近未标记的店中距离小于等于eps的点加入聚类中，并标记
            for item_index in self.items_within_eps(core, items):
                if labels[item_index] == -1:
                    clusters[label].append(item_index)
                    labels[item_index] = label


        # 此时label仍为-1的点为outlier

        # 返回各聚类
        log.info("cluster size: %d"%(len(clusters)))
        return clusters

    def items_within_eps(self, item, items):
        # TODO: 实现 {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}
        return self._brute(item, items)

    def _ball_tree(self, item, items):
        # TODO
        pass

    def _kd_tree(self, item, items):
        # TODO
        pass

    def _brute(self, item, items):
        return list(filter(lambda i: self.distance(item, items[i]) <= self.eps, range(len(items))))


    def distance(self, lhs: tuple, rhs: tuple) -> float:
        # TODO: 实现其他距离度量方法
        import math
        return math.sqrt(super().distance(lhs, rhs))


if __name__ == '__main__':
    from utils.functions import test_iris
    test_iris(DBSCAN(3, 5))