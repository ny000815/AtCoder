N, Y = map(int, input().split())
resa, resb, resc = -1, -1, -1
for i in range(N + 1):
  for j in range(N + 1):
    k = N - i - j
    if i * 10000 + j * 5000 + k * 1000 == Y and k >= 0:
      resa, resb, resc = i, j, k
print(resa, resb, resc)