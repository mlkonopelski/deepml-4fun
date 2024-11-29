'''Write a Python function to create a batch iterator for the samples in a numpy array X and an optional numpy array y. The function should yield batches of a specified size. If y is provided, the function should yield batches of (X, y) pairs; otherwise, it should yield batches of X only.

```
Example:
X = np.array([[1, 2], 
            [3, 4], 
            [5, 6], 
            [7, 8], 
            [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
batch_iterator(X, y, batch_size)
output:
[[[[1, 2], [3, 4]], [1, 2]],
    [[[5, 6], [7, 8]], [3, 4]],
    [[[9, 10]], [5]]]
```
Reasoning:
The dataset X contains 5 samples, and we are using a batch size of 2. Therefore, the function will divide the dataset into 3 batches. The first two batches will contain 2 samples each, and the last batch will contain the remaining sample. The corresponding values from y are also included in each batch.
    '''

import numpy as np

def chunk(list, chunk_size):
    for i in range(0, len(list), chunk_size):
        yield list[i:i+chunk_size]


def batch_iterator(X, y=None, batch_size=64):

    # ixs = chunked(list(range(X.shape[0])), batch_size)
    results = []
    for chunk_ix in chunk(list(range(X.shape[0])), batch_size):
        if not isinstance(y, np.ndarray):
            results.append(X[chunk_ix].tolist())
        else:
            results.append([X[chunk_ix].tolist(), y[chunk_ix].tolist()])

    return results


if __name__ == '__main__':
    
    X = np.array([[1, 2], 
                [3, 4], 
                [5, 6], 
                [7, 8], 
                [9, 10]])
    y = np.array([1, 2, 3, 4, 5])
    batch_size = 2

    target = [[[[1, 2], [3, 4]], [1, 2]],
            [[[5, 6], [7, 8]], [3, 4]],
            [[[9, 10]], [5]]]

    result = batch_iterator(X, y, batch_size)
    print(result)