# 实现的聚类算法集（接口参照[scikit-learn](http://scikit-learn.org/stable/modules/classes.html#classes))
1. [x] K-means
    1. [x] basic version
    2. [x] mini-batch
    3. [x] bisecting
2. [x] DBSCAN
3. [ ] [X-means](https://stats.stackexchange.com/questions/169319/x-means-algorithm-and-bic)
4. [x] K-medoid
5. [ ] //__this is Classification//[Learning vector quantization](http://machinelearningmastery.com/learning-vector-quantization-for-machine-learning/)
6. [ ] [Shared Nearest Neighbor Clustering](https://www.cise.ufl.edu/class/cis4930sp09dm/notes/dm5part5.pdf)
7. [x] Hierarchical(divisive VS agglomerative)
    1. [x] min
    2. [x] max
    3. [x] average
    4. [x] centroid
    5. [x] [Minimum energy clustering](https://en.wikipedia.org/wiki/Energy_distance)
    6. [x] [Ward](https://en.wikipedia.org/wiki/Ward%27s_method)
8. [ ] Affinity Propagation
9. [ ] Mean-Shift
10. [ ] Spectral Clustering
11. [ ] Chameleon
12. [ ] Birch
13. [ ] Gaussian Mixtures
14. [ ] Kernel K-Means
15. [ ] //ISODATA
16. [ ] //Fuzzy-means
17. [ ] //DENCLUE
18. [ ] Jarvis-Patrick Clustering
19. [ ] //Hypergraph-based Clustering
20. [ ] //ROCK
21. [ ] CURE
22. [ ] //CLIQUE
23. [ ] //Bubble
24. [ ] //Wave Cluster
25. [ ] //MAFIA

> [聚类算法汇总](http://blog.chinaunix.net/uid-10289334-id-3758310.html) <br>
> 实现上述算法之后,可以从该参考文章中挑选另外一些出来进行实现

> [数据常青藤](http://www.dataivy.cn/blog/category/unsupervised-learning/clustering/)

# 评价标准
## Intrinsic Evaluation Methods
// Sum of squares
// Silhouette index(mean)
// Davies–Bouldin index
// Dunn index

// Calinski-Harabasz
// R-squared index
// Hubert-Levin (C-index)
// ##Krzanowski-Lai index // determine the number of clusters
// Modified Hubert Γ statistic
// ##Hartigan index // determine the number of clusters
// Root-mean-square standard deviation (RMSSTD) index
// ---Semi-partial R-squared (SPR) index
// ---Distance between two clusters (CD) index
// ---weighted inter-intra index
// ---Homogeneity index
// ---Separation index

4. [](http://scikit-learn.org/stable/modules/classes.html#clustering-metrics)
[](https://classes.soe.ucsc.edu/bme210/Winter04/lectures/Bio210w04-Lect09-ClusterEvaluation.pdf)
[](https://stats.stackexchange.com/questions/21807/evaluation-measure-of-clustering-without-having-truth-labels)
[](https://cran.r-project.org/web/packages/clusterCrit/vignettes/clusterCrit.pdf)
# 数据生成及数组操作
1. [NumPy](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)

# 可视化
1. [matplotlib](http://matplotlib.org/)
2. [pyplot](http://matplotlib.org/users/pyplot_tutorial.html)


[](http://scikit-learn.org/stable/modules/classes.html#clustering-metrics)
[](http://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XL-7/71/2014/isprsarchives-XL-7-71-2014.pdf)
[](http://datamining.rutgers.edu/publication/internalmeasures.pdf)
[](http://www.inf.ufpr.br/lesoliveira/padroes/validity_index.pdf)
[](http://www.biomedcentral.com/content/supplementary/1477-5956-9-30-S4.PDF)