# Project Euler 04

# A palindromic number reads the same both ways. The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

largest_palindrome = 0

number_1 = 100
number_2 = 100

while number_1 < 1000:
  product = number_1 * number_2
  number_1 += 1
  if product == (int(str(product)[::-1])):
      while product > largest_palindrome:
        largest_palindrome = product
  if number_1 == 999:
    number_2 += 1
    number_1 = 100
    if number_2 == 1000:
      break

print(largest_palindrome)
