# Project Euler 01

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


numbers = list(range(0, 1001))
numbers_3_5 = []

for i in numbers:
   if (i % 3 == 0) or (i % 5 == 0):
     numbers_3_5.append(i)

print(sum(numbers_3_5))

# Shorter solution:
#numbers = list(range(0, 1001))
#sum = 0
#
#for i in numbers:
#  if (i % 3 == 0) or (i % 5 == 0):
#    sum += i
#print(sum)
