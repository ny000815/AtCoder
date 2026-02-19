from math import isqrt
N = int(input())

cnt = [0] * (N + 1)
for x in range(1, isqrt(N) + 1):
  y_max = isqrt(N - x ** 2)
  for y in range(x + 1, y_max + 1):
    cnt[x ** 2 + y ** 2] += 1

ans = [i for i in range(1, N + 1) if cnt[i] == 1]
print(len(ans))
print(*ans)