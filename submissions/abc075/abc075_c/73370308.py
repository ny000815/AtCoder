
import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

graph = [[False] * N for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  A, B = A - 1, B - 1
  graph[A][B] = True
  graph[B][A] = True

def dfs(v, visited):
  if visited[v]:
    return 
  visited[v] = True
  for i in range(N):
    if graph[v][i]:
      dfs(i, visited)

ans = 0
for i in range(N):
  for j in range(N):
    if graph[i][j]:
      graph[i][j] = False
      graph[j][i] = False
      visited = [False] * N
      dfs(0, visited)
      if sum(visited[i] for i in range(N)) != N:
        ans += 1
      graph[i][j] = True
      graph[j][i] = True

print(ans//2)
