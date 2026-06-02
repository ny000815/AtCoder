import sys
sys.setrecursionlimit(1000000)
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  graph[a].append(b)
  graph[b].append(a)

ans = 0
visited = [-1] * N
visited[0] = 1

def dfs(p, visited):
  global ans
  if not -1 in visited:
    ans += 1
    return
  for n in graph[p]:
    if visited[n] == -1:
      visited[n] = 1
      dfs(n, visited)
      visited[n] = -1

dfs(0, visited)
print(ans)