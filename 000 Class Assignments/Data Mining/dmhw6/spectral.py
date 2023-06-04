from point import Point
import numpy as np
from matplotlib import pyplot as plt
import time
global colors

from sklearn.cluster import SpectralClustering


colors = ["b","g","r","c","m","y","k",]


def get_distance_matrix(points: list[Point]):
    res = [[0 for i in range(len(points))] for j in range(len(points))]
    for i, pt1 in enumerate(points):
        for j, pt2 in enumerate(points):
            if pt1 == pt2:
                continue
            res[i][j] = pt1.dist(pt2)

    return res

points = [
(1,1), (0,3), (5,3), (6,2),
(7,2), (7,3), (8,4), (8,5),
(7,6), (6,5), (0,7), (1,6),
(1,8), (2,5), (2,7), (2,8),
(3,6), (3,7), (7,8), (9,9),
]

points = [Point(x=pt[0], y=pt[1]) for pt in points]
dist = get_distance_matrix(points)


sc = SpectralClustering(n_clusters=4, assign_labels='kmeans', n_neighbors=8, affinity='nearest_neighbors')

labels = sc.fit_predict(dist)

x = [pt.x for pt in points]
y = [pt.y for pt in points]
c = [ele + 1 for ele in labels]

plt.scatter(x, y, c=c)
plt.show()