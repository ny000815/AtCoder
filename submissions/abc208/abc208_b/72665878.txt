from math import factorial

P = int(input())
res = 0
for i in range(10, 0, -1):
  f = factorial(i)
  q = P // f
  res += q
  P -= q * f
print(res)