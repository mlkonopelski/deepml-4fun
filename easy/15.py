'''
Write a Python function that performs linear regression using gradient descent. The function should take NumPy arrays X (features with a column of ones for the intercept) and y (target) as input, along with learning rate alpha and the number of iterations, and return the coefficients of the linear regression model as a NumPy array. Round your answer to four decimal places. -0.0 is a valid result for rounding a very small number.

```Example:
input: X = np.array([[1, 1], [1, 2], [1, 3]]), y = np.array([1, 2, 3]), alpha = 0.01, iterations = 1000
output: np.array([0.1107, 0.9513])
reasoning: The linear model is y = 0.0 + 1.0*x, which fits the input data after gradient descent optimization.```
'''

import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
    m, n = X.shape
    theta = np.zeros((n, 1))

    for i in range(iterations):
        prediction = X @ theta
        error = prediction - y.reshape(-1, 1)
        gradient = X.T @ error / m
        theta -= alpha * gradient

        if i % 10 == 0:
            print(f'{i}: error: {error.sum().item()} theta: {theta.tolist()}')
    
    theta = theta.round(4).flatten()

    return theta


if __name__ == '__main__':

    comaprison_element_wise = linear_regression_gradient_descent(X = np.array([[1, 1], [1, 2], [1, 3]]), y = np.array([1, 2, 3]), alpha = 0.01, iterations = 1000) == np.array([0.1107, 0.9513])
    assert comaprison_element_wise.all() == np.True_