N = int(input())
A = list(map(int, input().split()))
cnt = 0
maxReach = 0

for i in range(N):
  if i > maxReach:
    break
  maxReach = max(maxReach, i + A[i] - 1)
  cnt += 1
print(cnt)