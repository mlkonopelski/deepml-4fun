'''
Write a Python function to perform a random shuffle of the samples in two numpy arrays, X and y, 
while maintaining the corresponding order between them.
 The function should have an optional seed parameter for reproducibility.
```Example:
X = np.array([[1, 2], 
                [3, 4], 
                [5, 6], 
                [7, 8]])
y = np.array([1, 2, 3, 4])
output: (array([[5, 6],
                [1, 2],
                [7, 8],
                [3, 4]]), 
            array([3, 1, 4, 2]))
```
'''

from typing import Tuple
import numpy as np
from numpy.typing import ArrayLike


def shuffle_data(X: ArrayLike, y: ArrayLike, seed=None) -> Tuple[ArrayLike, ArrayLike]:
    if seed:
        np.random.seed(seed)
    ixs = list(range(X.shape[0]))
    np.random.shuffle(ixs)
    
    return X[ixs], y[ixs]


if __name__ == '__main__':

    X = np.array([
        [1, 2], 
        [3, 4], 
        [5, 6], 
        [7, 8]])
    y = np.array([1, 2, 3, 4])

    result = shuffle_data(X, y, 42)
    print(result)