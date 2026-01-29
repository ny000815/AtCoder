
A, B = map(int, input().split())
for i in range (1, 1001):
  priceA = int(i * 0.08)
  priceB = int(i * 0.1)
  if priceA == A and priceB == B:
    print(i)
    break
  elif i == 1000:
    print(-1)