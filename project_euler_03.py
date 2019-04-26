# Project Euler 03

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

list_1 = list(range(3, 11))
prime_num = [2]
for i in list_1:
  num = 2
  while i > num:
    uitkomst = i / num
    if isinstance(uitkomst, int):
      break
    num += 1
  else:
    prime_num.append(i)

print(prime_num)

