#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.log import log
from algorithms.cluster import Cluster

class AgglomerativeClustering(Cluster):
    def __init__(self):
        pass

    def fit(self, items: list) -> list:
        # TODO
        # 将原始数据集分为n个聚类

        # 按照一定标准，每次将最相近的两个聚类合并，直到只剩k个聚类为止

        pass


if __name__ == '__main__':
    from utils.functions import test_iris
    test_iris(AgglomerativeClustering())