# Project Euler 03

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

list_1 = list(range(3, 1000))
prime_num = [2]
for i in list_1:
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


print(prime_num)

