N, K = map(int, input().split())
p = list(map(int, input().split()))

for i in range(N):
  p[i] = (p[i] + 1) / 2

prefixSum = [0] * (N + 1)
first = 0
for i in range(K):
  first += p[i]
prefixSum[K] = first
mx = prefixSum[K]

for i in range(K+1, N+1):
  prefixSum[i] = prefixSum[i-1] + p[i-1] - p[i - K -1]
  mx = max(mx, prefixSum[i])

print(mx)