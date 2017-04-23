#!/usr/bin/env python
# -*- coding: utf-8 -*-
from algorithms.kmeans import KMeans
from utils.log import log
import random


class MiniBatchKmeans(KMeans):
    def __init__(self, k, init='k-means++', max_iter=100, batch_size=100):
        super().__init__(k, max_iter, init)
        self.k = k
        self.batch_size = batch_size
        self.cluster_for = {}
        self.v = [0]*k

        log.debug("batch size %d"%batch_size)

    def update(self, centers, clusters, items):
        batch = self.get_batch(items)
        # 为样本中的各数据点找到其最近的中心
        for item_index, item in batch:
            self.cluster_for[(item_index, item)] = self.get_nearest_center(centers, item, item_index)

        # 根据个样本点更新其对应聚类中心
        dim = len(items[0])
        for item in batch:
            cluster_index = self.cluster_for[item]
            self.v[cluster_index] +=1
            u = 1/self.v[cluster_index]
            new_center = tuple((1-u)*centers[cluster_index][i]+u*item[KMeans.VALUE][i] for i in range(dim))

            if centers[cluster_index] != new_center:
                self.changed = True
            centers[cluster_index] = new_center

        # 如果已经结束，将每个点赋给其聚类
        if self.finished():
            for item_index, item in enumerate(items):
                cluster_index = self.get_nearest_center(centers, item, item_index)
                clusters[cluster_index].append((item_index, item))

    def get_batch(self, items):
        batch_size = min(self.batch_size, len(items)/3, 1)
        return [(i, items[i]) for i in random.sample(range(len(items)), batch_size)]


if __name__ == '__main__':
    from utils.functions import test_dummy_data, test_iris

    test_iris(MiniBatchKmeans(3))
