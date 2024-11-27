'''
Write a Python function that reshapes a given matrix into a specified shape.
```
Example:
    input: a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)
    output: [[1, 2], [3, 4], [5, 6], [7, 8]]
    reasoning: The given matrix is reshaped from 2x4 to 4x2.
```
'''

# too easy to use numpy
import numpy as np
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    reshaped_matrix = np.reshape(np.array(a), shape=new_shape).tolist()
    return reshaped_matrix

from itertools import batched # only for python 3.12+
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    
    reshaped_matrix = []
    for row in a:
        new_row = [list(col) for col in batched(row, n=new_shape[1])]
        reshaped_matrix.extend(new_row)

    return reshaped_matrix


if __name__ == '__main__':

    assert reshape_matrix([[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)) == [[1, 2], [3, 4], [5, 6], [7, 8]]
