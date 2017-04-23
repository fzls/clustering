#!/usr/bin/env python
# -*- coding: utf-8 -*-
from algorithms.cluster import Cluster
from utils.log import log


def data_iris() -> list:
    import csv
    from os.path import realpath, dirname, join

    data_path = realpath(join(dirname(realpath(__file__)), '../data/Iris.csv'))
    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        return [tuple(float(field) for field in record[:-1]) for record in list(reader)[1:]]


def _test(cluster: Cluster, data: list):
    log.info("\ndata: %s"%data)
    res = cluster.fit(data)
    log.info('\n'+'\n\n'.join(["Cluster %d: %s"%(c, r) for c, r in enumerate(res)]))


def test_iris(cluster: Cluster):
    _test(cluster, data_iris())


def test_dummy_data(cluster: Cluster):
    data = [
        (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),(1, 2), (1, 2), (1, 2),
        # (1, 2), (1, 2), (1, 2), (3, 4), (5, 6),
        # (100, 102), (104, 106),
        # (1001, 1005), (1009, 1010)
    ]
    _test(cluster, data)
