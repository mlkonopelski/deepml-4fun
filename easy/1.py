'''
Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector
Example:
```
input: a = [[1,2],[2,4]], b = [1,2]
output:[5, 10] 
reasoning: 1*1 + 2*2 = 5;
            1*2+ 2*4 = 10
```
'''

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    if any([len(a_row) != len(b) for a_row in a]):
        return -1
    c = [sum([a_ * b_ for a_, b_ in zip(a_row, b)]) for a_row in a] 
    return c


if __name__ == '__main__':

    a, b = [[1,2],[2,4]], [1,2]
    assert matrix_dot_vector(a, b) == [5, 10] 

    a, b = [[1,2],[2,4],[6,8],[12,4]], [1,2,3]
    assert matrix_dot_vector(a, b) == -1

    a, b  = [[1, 2, 3], [2, 4, 6]], [1, 2, 3]
    assert matrix_dot_vector(a, b) == [14, 28]
