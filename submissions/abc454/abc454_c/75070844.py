from collections import defaultdict
from collections import deque
N, M = map(int, input().split())
nodes = defaultdict(list)
for i in range(M):
  A, B = map(int, input().split())
  nodes[A].append(B)

visited = set()
q = deque()
q.append(1)
while q:
  curr = q.popleft()
  if curr in visited:
    continue
  visited.add(curr)
  for i in range(len(nodes[curr])):
    if nodes[curr][i] not in visited:
      q.append(nodes[curr][i])
print(len(visited))