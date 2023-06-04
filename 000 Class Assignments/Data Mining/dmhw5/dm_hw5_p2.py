from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plt
import numpy as np


def read_dataset(name: str):
	with open(f'{name}', 'r') as data:
		data.seek(0)
		reader = data.readlines()
		dataset = []
		for line in reader:
			res = line.strip().split(' ')
			res = [float(ele) for ele in res]
			res[-1] = int(res[-1])
			dataset += [res]
	return dataset

def train_and_graph():

	training_1 = read_dataset('dataset1_training.txt')
	testing_1 = read_dataset('dataset1_testing.txt')

	training_data = [elem[0:2] for elem in training_1]
	target = [elem[-1] for elem in training_1]

	x_train, x_test, y_train, y_test = train_test_split(training_data, target, test_size=0.3)

	clf = svm.SVC(kernel='linear')
	clf.fit(x_train, y_train)
	y_pred = clf.predict(x_test)

	print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
	print("Precision:",metrics.precision_score(y_test, y_pred))
	print("Recall:",metrics.recall_score(y_test, y_pred))

	test = [elem[:2] for elem in testing_1]
	ans = [elem[-1] for elem in testing_1]
	predictions = list(clf.predict(test))


	x = [elem[0] for elem in test]
	y = [elem[1] for elem in test]

	w = clf.coef_[0]
	b = clf.intercept_[0]
	x_points = np.linspace(min(x), max(x))
	y_points = -(w[0] / w[1]) * x_points - b / w[1]

	fig, ax = plt.subplots()
	ax.scatter(x, y, c=predictions, alpha=0.5)
	ax.plot(x_points, y_points, c='r',)
	plt.show()


def train_and_graph2():

	training_1 = read_dataset(f'dataset2_training.txt')
	testing_1 = read_dataset(f'dataset2_testing.txt')

	training_data = [elem[0:2] for elem in training_1]
	target = [elem[-1] for elem in training_1]

	x_train, x_test, y_train, y_test = train_test_split(training_data, target, test_size=0.3)

	clf = svm.SVC(kernel='poly')
	clf.fit(x_train, y_train)
	y_pred = clf.predict(x_test)

	print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
	print("Precision:",metrics.precision_score(y_test, y_pred))
	print("Recall:",metrics.recall_score(y_test, y_pred))


	test = [elem[:2] for elem in testing_1]
	ans = [elem[-1] for elem in testing_1]
	predictions = clf.predict(test)

	x = [elem[0] for elem in test]
	y = [elem[1] for elem in test]

	xmin = min(x) - 1
	xmax = max(x) + 1
	ymin = min(y) - 1
	ymax = max(y) + 1
	h = .01

	xx, yy = np.meshgrid(np.arange(xmin, xmax, h), np.arange(ymin, ymax, h))
	z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
	z = z.reshape(xx.shape)

	fig, ax = plt.subplots()
	ax.contour(xx, yy, z)

	ax.scatter(x, y, c=predictions, alpha=0.5)
	plt.show()

train_and_graph()
train_and_graph2()

