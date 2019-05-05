# Project Euler 05

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
# any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1
# to 20?

smallest_number = 20
divider = 20

while divider >= 1:
  if smallest_number % divider == 0:
    divider -= 1
    if divider == 1:
      solution = smallest_number
      break
  else:
    smallest_number += 20
    divider = 20

print(solution)

