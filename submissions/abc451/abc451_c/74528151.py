import heapq
Q = int(input())
a = []
heapq.heapify(a)
for _ in range(Q):
  t, h = map(int, input().split())
  if t == 1:
    heapq.heappush(a, h)
  else:
    while a and a[0] <= h:
      heapq.heappop(a)
  print(len(a))