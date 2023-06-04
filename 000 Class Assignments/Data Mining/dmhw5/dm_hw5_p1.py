import random as ran
from math import exp
from matplotlib import pyplot as plt
from sklearn import svm

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




# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[ran.random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[ran.random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network



# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation


# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))


# Forward propagate input to a network output
def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs




# Calculate the derivative of an neuron output
def transfer_derivative(output):
	return output * (1.0 - output)

# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(neuron['output'] - expected[j])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])


# Update network weights with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] -= l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] -= l_rate * neuron['delta']



# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[row[-1]] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))




# Make a prediction with a network
def predict(network, row):
	outputs = forward_propagate(network, row)
	return outputs.index(max(outputs))







training_1 = read_dataset('dataset1_training.txt')
testing_1 = read_dataset('dataset1_testing.txt')
network = initialize_network(2, 4, 2)


train_network(network=network, train=training_1, l_rate=0.8, n_epoch=1, n_outputs=2)
predictions = [predict(network, row) for row in testing_1]
x = [elem[0] for elem in testing_1]
y = [elem[1] for elem in testing_1]
plt.scatter(x, y, c=predictions, alpha=0.5)
plt.show()

train_network(network=network, train=training_1, l_rate=0.8, n_epoch=3, n_outputs=2)
predictions = [predict(network, row) for row in testing_1]
x = [elem[0] for elem in testing_1]
y = [elem[1] for elem in testing_1]
plt.scatter(x, y, c=predictions, alpha=0.5)
plt.show()

train_network(network=network, train=training_1, l_rate=0.8, n_epoch=10, n_outputs=2)
predictions = [predict(network, row) for row in testing_1]
x = [elem[0] for elem in testing_1]
y = [elem[1] for elem in testing_1]
plt.scatter(x, y, c=predictions, alpha=0.5)
plt.show()











training_2 = read_dataset('dataset2_training.txt')
testing_2 = read_dataset('dataset2_testing.txt')
network = initialize_network(2, 4, 2)

train_network(network=network, train=training_2, l_rate=0.8, n_epoch=1, n_outputs=2)
predictions = [predict(network, row) for row in testing_2]
x = [elem[0] for elem in testing_2]
y = [elem[1] for elem in testing_2]
plt.scatter(x, y, c=predictions, alpha=0.5)
plt.show()

train_network(network=network, train=training_2, l_rate=0.8, n_epoch=15, n_outputs=2)
predictions = [predict(network, row) for row in testing_2]
x = [elem[0] for elem in testing_2]
y = [elem[1] for elem in testing_2]
plt.scatter(x, y, c=predictions, alpha=0.5)
plt.show()

train_network(network=network, train=training_2, l_rate=0.8, n_epoch=100, n_outputs=2)
predictions = [predict(network, row) for row in testing_2]
x = [elem[0] for elem in testing_2]
y = [elem[1] for elem in testing_2]
plt.scatter(x, y, c=predictions, alpha=0.5)
plt.show()


