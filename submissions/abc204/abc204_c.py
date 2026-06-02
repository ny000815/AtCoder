import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

aL = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  A, B = A - 1, B - 1
  aL[A].append(B)
for i in range(N):
  aL[i].append(i)

reachable = [[0] * N for _ in range(N)]


def dfs(v):
  if dest[v]:
    return
  dest[v] = True
  for v2 in aL[v]:
    dfs(v2)

ans = 0
for i in range(N):
  dest = [False] * N
  dfs(i)
  ans += sum(dest)

print(ans)