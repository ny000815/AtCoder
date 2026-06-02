N = int(input())
A = list(map(int, input().split()))
maximum = 0
preSum, bPreSum = [0] * (N+1), [0] * (N + 1)
seen = set()
for i in range(N):
  seen.add(A[i])
  preSum[i+1] = len(seen)
#print(preSum)

seen = set()
for i in range(N-1, -1, -1):
  seen.add(A[i])
  bPreSum[i] = len(seen)
#print(bPreSum)

for i in range(N+1):
  a1, a2 = 0, 0
  maximum = max(maximum, preSum[i] + bPreSum[i])
print(maximum)