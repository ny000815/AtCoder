N, M = map(int, input().split())
graph = [False]*N
ans = 0

edges = [[] for _ in range(N)]
for _ in range(M):
  v1, v2 = map(int, input().split())
  v1 -= 1
  v2 -= 1
  edges[v1].append(v2)
  edges[v2].append(v1)

def dfs(n):
  graph[n] = True
  for nextNode in edges[n]:
    if not graph[nextNode]:
      dfs(nextNode)

for i in range(N):
  if not graph[i]:
    dfs(i)
    ans += 1
print(ans)