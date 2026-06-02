N, K = map(int, input().split())
H = list(map(int, input().split()))

cost = [10 ** 100 for _ in range(N)]
cost[0] = 0

for i in range(N):
  for j in range(i, i + K + 1):
    if j >= N:
      continue
    cost[j] = min(cost[j], abs(H[j] - H[i]) + cost[i])
print(cost[N-1])
