N, M, X = map(int, input().split())
A = []
for i in range(N):
  A.append(list(map(int, input().split())))
ALL = 1 << N

def hasBit(n, i):
  return n & (1 << i)

values = [[0]*(M + 1) for _ in range(ALL)]

ans = 10 ** 100
for n in range(ALL):
  for i in range(N):
    if hasBit(n, i):
      for j in range(M + 1):
        values[n][j] += A[i][j]
      OverT = True
      for j in range(1, M + 1):
        if values[n][j] < X:
          OverT = False
      if OverT:
        ans = min(ans, values[n][0])
if ans == 10 ** 100:
  ans = -1
print(ans)