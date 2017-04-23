#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from algorithms.cluster import Cluster
from utils.log import log


class KMeans(Cluster):
    def __init__(self, n_clusters: int, max_iter=100, init='k-means++', n_init=10, tol=0.0001, ):
        """
        :param n_clusters: 聚类个数
        :param max_iter: 迭代次数上限
        """
        # TODO: 添加剩余参数的支持
        self.n_clusters = n_clusters
        self.changed = False
        self.max_iter = max_iter

    def fit(self, items: list) -> list:
        """
        对数据集进行聚类并返回聚类结果
        :param items: 需要聚类的数据集，每个数据为用list表示。eg. [ [1, 2], [1, 3], [2, 4] .... , [42, 2] ]
        :return: 聚类结果（用在原数据集中的下标来代表该数据）。eg. [ [0, 3, 4], [1, 2, 5], [6, 7, 8] ]
        """
        # 初始化聚类中心和聚类
        # TODO: 1.random 2. kmeans++
        items = [tuple(item) for item in items]
        centers = self.init(items)
        clusters = [[] for cluster in range(self.n_clusters)]

        iter = 0
        while True:
            iter += 1
            self.changed = False

            self.update_clusters(centers, items, clusters)
            log.debug('\n[cluster]: %s\n[center]: %s' % (clusters, centers))
            self.update_centers(centers, items, clusters)

            if self.finished(iter):
                break
        log.info(iter)

        return clusters

    def update_centers(self, centers: list, items: list, clusters: list) -> None:
        """
        更新聚类中心
        :param centers: 聚类中心
        :param items: 数据集
        :param clusters: 聚类
        """
        for cluster_index, cluster in enumerate(clusters):
            new_center = self.get_new_center(cluster, items)
            if centers[cluster_index] != new_center:
                self.changed = True
            centers[cluster_index] = new_center

    def get_new_center(self, cluster: list, items: list) -> tuple:
        """获取新的聚类中心（通过取聚类中各数据的中心值）"""
        dim = len(items[0])
        _sum = [0 for i in range(dim)]
        for item_index in cluster:
            for i in range(dim):
                _sum[i] += items[item_index][i]
        new_center = tuple(_s / len(cluster) for _s in _sum)
        return new_center

    def update_clusters(self, centers: list, items: list, clusters: list) -> None:
        """
        更新聚类
        :param centers: 聚类中心
        :param items: 数据集
        :param clusters: 聚类结果
        """
        # 清除原先的聚类结果
        for cluster in clusters:
            cluster.clear()

        # 根据当前聚类中心得到新的聚类结果
        for item_index, item in enumerate(items):
            # 找到与该数据点最接近的聚类中心
            nearest_cluster_index = 0
            for cluster_index, center in enumerate(centers):
                if self.distance(center, item) < self.distance(centers[nearest_cluster_index], item):
                    nearest_cluster_index = cluster_index

            # 将该数据点分配到该聚类中心所在聚类
            clusters[nearest_cluster_index].append(item_index)

    def init(self, items: list) -> list:
        """初始化聚类中心"""
        return self.init_random(items)

    def init_random(self, items: list) -> list:
        """
        随机选择k个元素作为初始蕨类中心
        """
        return random.sample(items, self.n_clusters)

    def init_kmeans_plus_plus(self, items: list) -> list:
        """选择k个尽可能相隔较远的元素作为初始聚类中心"""
        # TODO: test
        pass
        return []

    def finished(self, iter: int) -> bool:
        """判断是否可以结束算法"""
        return not self.changed or iter >= self.max_iter


if __name__ == '__main__':
    from utils.functions import test_iris
    test_iris(KMeans(3))
