from matplotlib import pyplot as plt
from point import Point


global colors
colors = ["b","g","r","c","m","y","k",]


def k_means(k, points: list, show_iterations=False):
	if k <= 1:
		raise Exception('Invalid k value')
	elif len(points) < k:
		raise Exception('Invalid k for the amount of points')
	elif len(colors) < k:
		raise Exception('Not enough colors')
	
	# initialize arbitrary centers for kth cluster
	center = []
	for i in range(k):
		points[i].set_color(colors[i])
		center += [points[i]]

	# initial clustering 
	clustering = {
	'no_group' : set(points),
	'centers': set(center)
	}

	# initialize keys for cluster names inside dictionary
	for ele in center:
		clustering[ele.color] = {ele}

	# call recursive function
	if show_iterations:
		_k_means(k=k, clusters=clustering, all_points=points)
	else:
		_k_means(k=k, clusters=clustering)



# finds closest clustering for a given point
def closest_center(centers: set, point: Point):
	closest = min(centers, key=lambda x: x.dist(point))
	return closest


# recalculates mean x,y coordinates for all clusters
def recalculate_centers(clusters: dict):
	# keep old means to check if there is a change
	old = {}
	for ele in clusters['centers']:
		old[ele.color] = ele
	clusters['centers'].clear()
	
	# calculate new mean
	for color in old.keys():
		size = len(clusters[color])
		x = sum([pt.x for pt in clusters[color]]) // size
		y = sum([pt.y for pt in clusters[color]]) // size
		clusters['centers'].add(Point(x, y, color=color))

	# check if mean changed for a cluster. If any changed, we return True
	for ele in clusters['centers']:
		if not old[ele.color].__cmp__(ele):
			return True
	return False				


def _k_means(k, clusters: dict(), all_points = []):
	if all_points:
		graph_points(all_points)

	# first round, no assignment for points initially
	if 'no_group' in clusters: 
		for pt in clusters['no_group']:
			closest = closest_center(centers=clusters['centers'], point=pt)
			pt.set_color(closest.color)
			clusters[closest.color].add(pt)
		clusters.pop('no_group')
		res = recalculate_centers(clusters)
		if res:	# if there was a change, continue
			_k_means(k=k, clusters=clusters, all_points=all_points)

	else:
		for k, points in clusters.items():
			if k == 'centers':
				continue

			changed = set()
			for pt in points:
				closest = closest_center(clusters['centers'], pt) 
				if closest.color != pt.color:
					pt.color = closest.color
					clusters[closest.color].add(pt)
					changed.add(pt)

			for pt in changed:
				clusters[k].remove(pt)

		res = recalculate_centers(clusters)
		if res:		# if there was a change in means
			_k_means(k=k, clusters=clusters, all_points=all_points)
		return

# function used to see changes in clustering after each iteration
def graph_points(points):
	x = [pt.x for pt in points]
	y = [pt.y for pt in points]
	color = [pt.color for pt in points]
	plt.scatter(x, y, c=color, s=200)
	plt.show()





points = [
(1,1), (0,3), (5,3), (6,2),
(7,2), (7,3), (8,4), (8,5),
(7,6), (6,5), (0,7), (1,6),
(1,8), (2,5), (2,7), (2,8),
(3,6), (3,7), (7,8), (9,9),
]

points = [Point(x=pt[0], y=pt[1]) for pt in points]

k_means(3, points)

x = [pt.x for pt in points]
y = [pt.y for pt in points]
color = [pt.color for pt in points]
plt.scatter(x, y, c=color)
plt.show()