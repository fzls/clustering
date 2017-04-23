#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from functools import lru_cache


class Cluster(object):
    @lru_cache()
    def distance(self, lhs: tuple, rhs: tuple) -> float:
        """
        返回两个数据点之间的距离
        :param lhs:
        :param rhs:
        :return:
        """
        dim = len(rhs)
        dis = 0
        for d in range(dim):
            dis += math.pow(rhs[d] - lhs[d], 2)

        return dis

    def fit(self, items: list) -> list:
        raise NotImplementedError("必须实现该方法")