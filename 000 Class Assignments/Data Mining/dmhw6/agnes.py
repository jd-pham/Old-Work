from point import Point
import numpy as np
from matplotlib import pyplot as plt
import time

global colors
colors = ["b","g","r","c","m","y","k",]



def find_cluster(points: list[Point]):
    res = []
    for i, pt1 in enumerate(points):
        for j, pt2 in enumerate(points):
            if pt1 == pt2:
                continue
            if type(pt1) == list or type(pt2) == list:
            
                if type(pt1) == list:
                    if type(pt2) == list:  # pt1 == list, pt2 == list
                        for ele in pt1:
                            for ele2 in pt2:
                                dist = ele.dist(ele2)
                                res += [[dist, i, j]]
                    
                    else:       # pt1 == list, pt2 != list
                        for ele in pt1:
                            dist = ele.dist(pt2)
                            res += [[dist, i, j]]
                
                else:       # pt1 != list, pt2 == list
                    for ele in pt2:
                        dist = ele.dist(pt1)
                        res += [[dist, i, j]]
            
            else:
                dist = pt1.dist(pt2)
                res += [[dist, i, j]]
    
    res = sorted(res, key=lambda x: x[0])
    return res[0][1], res[0][2]

def AGNES(points: list[Point], k):

    while len(points) > k:
        i, j = find_cluster(points)

        res = []
        if type(points[i]) == list:
            res += [ele for ele in points[i]]
        if type(points[j]) == list:
            res += [ele for ele in points[j]]
        
        if not res:
            cluster = [points[i], points[j]]
        else:
            cluster = res
        points = [ele for ele in points if ele != points[i] or ele != points[j]]
        points = [points[k] for k in range(len(points)) if k != i and k != j]
        points.append(cluster)
        print(points)
        
    for i, ele in enumerate(points):
        if type(ele) != Point:
            for ele2 in ele:
                plt.scatter(ele2.x, ele2.y, c=colors[i])
        else:
            plt.scatter(ele.x, ele.y, c=colors[i])
    plt.show()






points = [
(1,1), (0,3), (5,3), (6,2),
(7,2), (7,3), (8,4), (8,5),
(7,6), (6,5), (0,7), (1,6),
(1,8), (2,5), (2,7), (2,8),
(3,6), (3,7), (7,8), (9,9),
]


points = [Point(x=pt[0], y=pt[1]) for pt in points]

AGNES(points, 2)

