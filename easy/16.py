'''
Write a Python function that performs feature scaling on a dataset using both standardization and min-max normalization. The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. It should return two 2D NumPy arrays: one scaled by standardization and one by min-max normalization. Make sure all results are rounded to the nearest 4th decimal.
```Example:
input: data = np.array([[1, 2], [3, 4], [5, 6]])
output: ([[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]], [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]])
reasoning: Standardization rescales the feature to have a mean of 0 and a standard deviation of 1.
Min-max normalization rescales the feature to a range of [0, 1], where the minimum feature value
maps to 0 and the maximum to 1.```
'''

import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):

    standardized_data = (data - data.mean(axis=0)) / data.std(axis=0)
    standardized_data = standardized_data.round(4)
    
    min, max = data.min(axis=0), data.max(axis=0)
    normalized_data = (data - min) / (max - min)
    normalized_data = normalized_data.round(4)

    return standardized_data, normalized_data


if __name__ == '__main__':

    standardized_data, normalized_data = feature_scaling(np.array([[1, 2], [3, 4], [5, 6]])) 
    assert (standardized_data == [[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]]).all() == True
    assert (normalized_data == [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]]).all() == True
