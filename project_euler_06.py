#Project Euler 06

# The sum of the squares of the first ten natural numbers is,
# 1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and
# the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural 
# numbers and the square of the sum.

import numpy as np

array_100 = np.arange(1, 101)
array_square = array_100 ** 2
sum_array = np.sum(array_square)

array_sum_100 = np.sum(array_100)
square_sum_100 = array_sum_100 ** 2

solution = square_sum_100 - sum_array

print(solution)
