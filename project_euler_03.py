# Project Euler 03

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def calc_prime_num(max_num):
  input_range = list(range(3, (max_num + 1)))
  prime_num = [2]
  for i in input_range:
    num = 2
    while i >= num:
      if i == num:
        prime_num.append(i)
        break

      uitkomst = i / num
      if uitkomst.is_integer():
        break
      elif not uitkomst.is_integer():
        num += 1
  return prime_num

def calc_prime_factors(number, prime_numbers):
  factors = []
  for prime in prime_numbers:
    while number.is_integer():
      uitkomst = number / prime
      if uitkomst.is_integer():
        factors.append(prime)
        number = uitkomst
        if uitkomst == 1.0:
          print(factors)
          exit()
      elif not uitkomst.is_integer():
        break

prime_numbers = calc_prime_num(10000)
number = float(600851475143)
calc_prime_factors(number, prime_numbers)



