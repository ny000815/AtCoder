N = int(input())
P = [0] + list(map(int, input().split()))

maxScore = sum(P)

dp = [[0] * (maxScore + 1) for _ in range(N + 1)]

dp[0][0] = 1

for i in range(1, N + 1):
  for j in range(0, maxScore + 1):
    if dp[i - 1][j]:
      dp[i][j] = 1
    if j >= P[i] and dp[i - 1][j - P[i]]:
      dp[i][j] = 1

print(sum(dp[N]))