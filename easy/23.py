'''Write a Python function that computes the softmax activation for a given list of scores. The function should return the softmax values as a list, each rounded to four decimal places.
```Example:
input: scores = [1, 2, 3]
output: [0.0900, 0.2447, 0.6652]
reasoning: The softmax function converts a list of values into a probability distribution. The probabilities are proportional to the exponential of each element divided by the sum of the exponentials of all elements in the list.
```
'''

import math

def softmax(scores: list[float]) -> list[float]:
    exp_sum = sum([math.exp(s) for s in scores])
    probabilities = [round(math.exp(s) / exp_sum, 4) for s in scores]
    return probabilities


if __name__ == '__main__':
    
    assert softmax([1, 2, 3]) == [0.0900, 0.2447, 0.6652]
