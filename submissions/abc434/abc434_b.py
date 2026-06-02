from collections import defaultdict
N, M = map(int, input().split())
counts = defaultdict(list)
for i in range(N):
  A, B = map(int, input().split())
  counts[A].append(B)

for i in range(1,M+1):
  print(sum(counts[i])/len(counts[i]))