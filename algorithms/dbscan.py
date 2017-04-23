#!/usr/bin/env python
# -*- coding: utf-8 -*-
from algorithms.cluster import Cluster
from utils.log import log
from utils.metrics import distance


class DBSCAN(Cluster):
    def __init__(self, eps=0.5, min_samples=5):
        self.eps = eps
        self.min_samples = min_samples
        pass

    def fit(self, items: list):
        # 找到核心点
        cores = []
        for item_index, item in enumerate(items):
            # 计算与该点距离为eps的点的个数
            cnt = len(self.indexed_items_within_eps(item, items))
            # 将密度高于给定阈值的加入核心点中
            if cnt >= self.min_samples:
                cores.append((item_index, item))

            log.debug(list(sorted(map(lambda rhs: distance(item, rhs), items))[:4]))
        # 将核心点eps范围内的点标记为其聚类内的点
        clusters = []
        cluster_label = -1
        labels = {}
        for core in cores:
            # 若该核心点未被标记过，则新建一个聚类，否则获得其聚类标号
            if labels.get(core) is None:
                clusters.append([])
                cluster_label += 1
                label = cluster_label
            else:
                label = labels[core]

            # 将该核心点附近未标记的店中距离小于等于eps的点加入聚类中，并标记
            for indexed_item in self.indexed_items_within_eps(core[self.VALUE], items):
                if labels.get(indexed_item) is None:
                    clusters[label].append(indexed_item)
                    labels[indexed_item] = label

        # 此时label仍为-1的点为outlier

        # 返回各聚类
        log.info("cluster size: %d" % (len(clusters)))
        return clusters

    def indexed_items_within_eps(self, item, items):
        # TODO: 实现 {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}
        return self._brute(item, items)

    def _ball_tree(self, item, items):
        # TODO
        pass

    def _kd_tree(self, item, items):
        # TODO
        pass

    def _brute(self, item, items):
        return list(
            filter(lambda indexed_item: distance(item, indexed_item[self.VALUE]) <= self.eps, enumerate(items)))


if __name__ == '__main__':
    from utils.functions import test_iris

    test_iris(DBSCAN(3, 5))
