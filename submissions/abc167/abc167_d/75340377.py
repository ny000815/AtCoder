from collections import defaultdict
N, K = map(int, input().split())
A = [0]+ list(map(int, input().split()))
visited = set()
visited.add(1)
curr = A[1]
route = [1]
for _ in range(N):
  if curr in visited:
    lst = curr
    break
  route.append(curr)
  visited.add(curr)
  curr = A[curr]
loopstart = route.index(lst) -1
looproute = route[route.index(lst):]
if K >= len(route):
  num = (K - len(route)) % len(looproute)
  print(looproute[num])
else:
  print(route[K])