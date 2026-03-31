N = int(input())
A = []
for i in range(N-1):
    A.append([0]*(i+1) + list(map(int, input().split())))
ALL = 1 << N

def hasBit(n, i):
  return n & (1 << i)

happy = [0] * ALL
for n in range(ALL):
  for i in range(N - 1):
    for j in range(N):
      if hasBit(n, i) and hasBit(n, j):
        happy[n] += A[i][j]

ans = -10 ** 100

for i in range(ALL):
  for j in range(ALL):
    if i & j:
      continue
    k = ALL - 1 - (i | j)
    ans = max(ans, happy[i]+happy[j]+happy[k])
print(ans)