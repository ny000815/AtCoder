N = int(input())
a = []
for i in range(N - 1):
  lst = list(map(int, input().split()))
  a.append([0] * (i + 1) + lst )

def checkBit(i, n):
  return n & 1 << i > 0

ALL = 1 << N
happy = [0] * ALL

for n in range(ALL):
  for i in range(N):
    for j in range(i + 1, N):
      if checkBit(i, n) and checkBit(j, n):
        happy[n] += a[i][j]

ans = -10 ** 100
for i in range(ALL):
  for j in range(ALL):
    if i & j > 0:
      continue
    k = ALL - 1 - (i | j)
    ans = max(ans, happy[i]+happy[j]+happy[k])
print(ans)