#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from functools import lru_cache
from utils.log import log


class Cluster(object):
    """
    clusters, cores 等中包含的item均以(item_index, item)的形式出现
    """
    INDEX = 0
    VALUE = 1
    #
    # @lru_cache()
    # def distance(self, lhs: tuple, rhs: tuple) -> float:
    #     """
    #     返回两个数据点之间的距离
    #     :param lhs:
    #     :param rhs:
    #     :return:
    #     """
    #     dim = len(rhs)
    #
    #     return math.sqrt(sum([(lhs[d] - rhs[d]) ** 2 for d in range(dim)]))

    def fit(self, items: list) -> list:
        raise NotImplementedError("必须实现该方法")

    def print(self, clusters):
        log.info('\n' + '\n\n'.join(["Cluster %d: %s" % (c, r) for c, r in enumerate(clusters)]))
