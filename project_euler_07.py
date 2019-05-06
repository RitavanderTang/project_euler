# Project Euler 07

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
# 6th prime is 13.

# What is the 10 001st prime number?

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
  return prime_num[10000]

prime_10001 = calc_prime_num(120000)
print(prime_10001)

