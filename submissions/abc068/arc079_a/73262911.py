from collections import deque
N, M = map(int, input().split())
graph = [[]*N for _ in range(N)]
dist = [500000] * N
dist[0] = 0
qeue = deque()
qeue.append(0)

for _ in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  graph[a].append(b)
  graph[b].append(a)

while qeue:
  i = qeue.popleft()
  for j in graph[i]:
    if dist[j] != 500000:
      continue
    dist[j] = dist[i] + 1
    qeue.append(j)

print("POSSIBLE" if dist[N-1] <= 2 else "IMPOSSIBLE")