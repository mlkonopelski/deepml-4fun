'''
Write a Python function that simulates a single neuron with a sigmoid activation function for binary classification, 
handling multidimensional input features. The function should take a list of feature vectors 
(each vector representing multiple features for an example), 
associated true binary labels, and the neuron's weights (one for each feature) and bias as input. 
It should return the predicted probabilities after sigmoid activation and the mean squared error 
between the predicted probabilities and the true labels, both rounded to four decimal places.
```
Example:
input: features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], labels = [0, 1, 0], weights = [0.7, -0.4], bias = -0.1
output: ([0.4626, 0.4134, 0.6682], 0.3349)
reasoning: For each input vector, the weighted sum is calculated by multiplying each feature by its corresponding weight, adding these up along with the bias, then applying the sigmoid function to produce a probability. The MSE is calculated as the average squared difference between each predicted probability and the corresponding true label.
```
'''


import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	
    probabilities = []
    for feature_vector in features:
        z = sum(feature * weight for feature, weight in zip(feature_vector, weights)) + bias
        prob = 1 / (1 + math.exp(-z))
        probabilities.append(round(prob, 4))

    mse = sum([(prob - label) ** 2 for prob, label in zip(probabilities, labels)]) / len(labels)

    return probabilities, round(mse, 4)


if __name__ == '__main__':

    probabilities, mse =  single_neuron_model(features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], labels = [0, 1, 0], weights = [0.7, -0.4], bias = -0.1)
    assert probabilities == [0.4626, 0.4134, 0.6682]
    assert mse == 0.3349
