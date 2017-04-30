#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import metrics
from utils.log import log


def avg(l):
    return sum(l) / len(l)


# 1
def ss_between_clusters(clusters, items):
    """max"""

    return sum([len(c) * metrics._centroid(c, items) ** 2 for c in clusters])


def _ss_within_cluster(c):
    return metrics.ssd(c)


# 2
def ss_within_clusters(clusters, items):
    """min"""
    return sum([_ss_within_cluster(c) for c in clusters])


def ss_between_within_cluster(c, items):
    b = len(c) * metrics._centroid(c, items) ** 2

    w = _ss_within_cluster(c)
    return w / b


# 3
def ss_between_within_clusters(clusters, items):
    """min"""
    return sum([ss_between_within_cluster(c, items) for c in clusters])


def _silhouette(c, clusters):
    def _(item):
        # avg dis to other items in cluster
        a = avg([metrics.distance(item, _item) for _item in c])

        # min dis to other cluster
        b = min([metrics._avg([item], c2) for c2 in clusters if c2 != c])

        return (b - a) / max(a, b)

    return avg([_(item) for item in c])
    pass


# 4
def silhouette(clusters, items):
    """max"""
    return avg([_silhouette(c, clusters) for c in clusters])
    pass


def _davies_bouldin_index_ci(ci, clusters):
    return max(
        [(metrics.avg_distance(ci) + metrics.avg_distance(cj)) / metrics._centroid(ci, cj) for cj in clusters if
         cj != ci])


# 5
def davies_bouldin_index(clusters, items):
    """min"""
    return avg([_davies_bouldin_index_ci(ci, clusters) for ci in clusters])


# 6
def dunn_index(clusters, items):
    """max"""
    n = len(clusters)
    # min distance between any clusters
    a = min([metrics._min(clusters[i], clusters[j]) for i in range(n) for j in range(i + 1, n)])
    # max avg distance in any cluster
    b = max([metrics.avg_distance(c) for c in clusters])

    return a / b


# 6
def calinski_harabasz(clusters, items):
    """max"""
    n = len(items)
    k = len(clusters)
    ss_b = ss_between_clusters(clusters, items)
    ss_w = ss_within_clusters(clusters, items)

    return (ss_b / (k - 1)) / (ss_w / (n - k))


# 7
def c_index(clusters, items):
    """min"""
    s_w = sum([metrics.distance(c[i], c[j]) for c in clusters for i in range(len(c)) for j in range(i + 1, len(c))])

    nw = sum(int(len(c) * (len(c) - 1) / 2) for c in clusters)
    paired_d = sorted(
        [metrics.distance(items[i], items[j]) for i in range(len(items)) for j in range(i + 1, len(items))])
    s_min = sum(paired_d[:nw])
    s_max = sum(paired_d[-nw:])

    return (s_w - s_min) / (s_max - s_min)


# 8
def r_squred(clusters, items):
    """max"""
    ss_total = metrics.ssd(items)
    ss_within = ss_within_clusters(clusters, items)
    ss_between = ss_total - ss_within
    # print('ss_between         : %s'%ss_between)
    # print('ss_between_clusters: %s'%ss_between_clusters(clusters, items))

    return ss_between / ss_total


# 9
def modified_hubert_γ_statistic(clusters, items):
    """max"""
    np = len(items) * (len(items) - 1) / 2

    cluster_for = {}
    for cluster in clusters:
        for item in cluster:
            cluster_for[item] = cluster

    from functools import reduce
    items = reduce(lambda s, c: s + c, clusters, [])

    s = sum([metrics.distance(items[i], items[j]) * metrics._centroid(cluster_for[items[i]], cluster_for[items[j]])
             for i in range(len(items))
             for j in range(i + 1, len(items))
             ])

    return s / np


# 10
def i_index(clusters, items):
    """max"""
    factor_1 = 1 / len(clusters)

    def _sum_of_distance_to_center(_items):
        m = metrics.avg_of_items(_items)
        return sum([metrics.distance(item, m) for item in _items])

    factor_2 = _sum_of_distance_to_center(items) / sum([_sum_of_distance_to_center(c) for c in clusters])

    factor_3 = max([metrics._centroid(clusters[i], clusters[j])
                    for i in range(len(clusters))
                    for j in range(i + 1, len(clusters))
                    ])

    p = 2

    return (factor_1 * factor_2 * factor_3) ** p


# 11
def xie_beni_index(clusters, items):
    """min"""
    _1 = ss_within_clusters(clusters, items)
    _2 = len(items) * min([metrics._centroid(clusters[i], clusters[j]) ** 2
                           for i in range(len(clusters))
                           for j in range(i + 1, len(clusters))])
    return _1 / _2


# 12
def rmsstd(clusters, items):
    """min"""
    _1 = ss_within_clusters(clusters, items)
    _2 = len(items[0][1]) * sum([len(c) - 1 for c in clusters])

    return (_1 / _2) ** 0.5


# 13
def adjusted_r_squred(clusters, items):
    """max"""
    n = len(items)
    k = len(clusters)
    ss_total = metrics.ssd(items)
    ss_within = ss_within_clusters(clusters, items)
    # ss_between = ss_total - ss_within
    # print('ss_between         : %s'%ss_between)
    # print('ss_between_clusters: %s'%ss_between_clusters(clusters, items))

    return 1 - (ss_within / (n - k - 1)) / (ss_total / (n - 1))


# 14
def sdbw_validity_index(clusters, items):
    """max"""

    def _(_items):
        return metrics.magnitude(metrics.variance_of_items(_items))

    k = len(clusters)

    scat = sum([_(c) for c in clusters]) / (k * _(items))
    # log.debug('scat: %s' % scat)

    limit = 1 / k * sum([_(c) for c in clusters])
    # log.debug('limit: %s' % limit)

    def __(ci, cj):
        def _f(x, y):
            return metrics.distance(x, y) <= limit
            pass

        def _(c):
            m = metrics.avg_of_items(c)
            return sum([_f(x, m) for x in c])

        _1 = _(ci + cj)
        _2 = max(_(ci), _(cj))

        return _1 / _2

    dens_bw = 1 / (k * (k - 1)) * sum([sum([__(ci, cj) for cj in clusters if cj != ci]) for ci in clusters])
    # log.debug('dens_bw: %s' % dens_bw)

    return scat + dens_bw

# 15
def ball_hall_index(clusters, items):
    """min"""
    k = len(clusters)
    return 1/k * sum([_ss_within_cluster(c)/len(c) for c in clusters])

# 16
def  banfeld_raftery_index(clusters, items):
    """min"""
    import math
    return sum([len(c) * math.log2(_ss_within_cluster(c) / len(c)) for c in clusters if len(c) > 1])

if __name__ == '__main__':
    items = [
        (100, 102), (104, 106), (103, 103), (101, 99),
        (1, 2), (3, 4), (5, 6),
        (1001, 1005), (1009, 1010), (1003, 1008)
    ]
    items = list(enumerate(items))
    log.debug(items)
    clusters_1 = [
        items[0:4],
        items[4:7],
        items[7:]
    ]
    clusters_2 = [
        items[0:3],
        items[3:8],
        items[8:]
    ]
    clusters_3 = [
        items[0:1],
        items[1:9],
        items[9:]
    ]
    log.debug(clusters_1)
    indexes = [
        ss_between_clusters,
        ss_within_clusters,
        ss_between_within_clusters,
        silhouette,
        davies_bouldin_index,
        dunn_index,
        calinski_harabasz,
        c_index,
        r_squred,
        modified_hubert_γ_statistic,
        i_index,
        xie_beni_index,
        rmsstd,
        adjusted_r_squred,
        sdbw_validity_index,
        ball_hall_index,
        banfeld_raftery_index
    ]
    for index in indexes:
        log.info('%30s(%3s) : %30s/%30s/%30s' % (
        index.__name__, index.__doc__, index(clusters_1, items), index(clusters_2, items), index(clusters_3, items)))

    fmt = '%23s'
    s = '\n%s' % [fmt % index.__name__ for index in indexes] \
        + '\n%s' % [fmt % index.__doc__ for index in indexes] \
        + '\n%s' % [fmt % index(clusters_1, items) for index in indexes] \
        + '\n%s' % [fmt % index(clusters_2, items) for index in indexes] \
        + '\n%s' % [fmt % index(clusters_3, items) for index in indexes]

    log.info(s)
    # log.info(metrics.variance_of_items(items))
    # log.info([metrics.variance_of_items(c) for c in clusters_1])
    # log.info([metrics.variance_of_items(c) for c in clusters_2])
    # log.info([metrics.variance_of_items(c) for c in clusters_3])