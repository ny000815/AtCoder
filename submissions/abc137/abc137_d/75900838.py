from heapq import heappush, heappop
N, M = map(int, input().split())
AtoB = [[]for i in range(M+1)]

for _ in range(N):
  A, B = map(int, input().split())
  if A > M:
    continue
  AtoB[A].append(B)

result = 0
que = []
for Bs in AtoB:
  for B in Bs:
    heappush(que, -B)
  if que:
    result += -heappop(que)
print(result)