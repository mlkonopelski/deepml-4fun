'''
Write a Python function that computes the transpose of a given matrix.
```
Example:
input: a = 
[[1,2,3],
 [4,5,6]]
output: 
[[1,4],
 [2,5],
 [3,6]]
reasoning: The transpose of a matrix is obtained by flipping rows and columns.
```
'''

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:

    b = []
    for col_ix in range(len(a[0])):
        b.append([row[col_ix] for row in a])
    return b


if __name__ == '__main__':
    a = [[1,2,3],[4,5,6]]
    assert transpose_matrix(a) == [[1,4],[2,5],[3,6]]