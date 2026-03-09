N, M = map(int, input().split())
edges = [[] for i in range(N+1)]
ans = 0
for _ in range(M):
  u, v = map(int, input().split())
  if u == v or v in edges[u]:
    #print(u, v)
    ans += 1
    continue
  edges[u].append(v)
  edges[v].append(u)
#print(edges)
print(ans)