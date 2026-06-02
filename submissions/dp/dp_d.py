N, W = map(int, input().split())
wi = []
vi = []
wi.append(0)
vi.append(0)
for _ in range(N):
  w, v = map(int, input().split())
  wi.append(w)
  vi.append(v)

dp = [[0] * (W+1) for _ in range(N + 1)]
for i in range(1, N + 1):
  for j in range(W+1):
    dp[i][j] = dp[i - 1][j]
    if j >= wi[i]:
      dp[i][j] = max(dp[i][j], dp[i - 1][j - wi[i]] + vi[i])

ans = 0
for i in range(W+1):
  ans = max(ans, dp[N][i])
print(ans)