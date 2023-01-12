#find the hcf of two numbers using Euclidian algorithm in python
def euclidean_algorithm(a, b):
  " Displays iterations of the euclidean algorithm "
  if b > a:
    # swap if necessary 
    # to ensure a is the larger number
    a, b = b, a

  while b:
    q = a // b
    r = a - q * b
    print(f'{a} = {q} x {b} + {r}') # use string interpolation to show formula
    a, b = b, r
    
  print(f'HCF = {a}')

  return a


a = int(input('First number: '))
b = int(input('Second number: '))
euclidean_algorithm(a, b)


# First number: 498
# Second number: 222
# 498 = 2 x 222 + 54
# 222 = 4 x 54 + 6
# 54 = 9 x 6 + 0
# HCF = 6


