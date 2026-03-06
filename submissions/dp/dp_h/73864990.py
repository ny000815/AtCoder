H, W = map(int, input().split())
a = []
for _ in range(H):
  a.append(input())
ans = [[0] * (W + 1) for _ in range(H + 1)]
ans[1][1] = 1
MOD = 1000000007
for i in range(1, H + 1):
  for j in range(1, W + 1):
    if j == 0 or a[i-1][j-1] == '#' or i == 1 and j == 1:
      continue
    ans[i][j] = (ans[i - 1][j] + ans[i][j - 1]) % MOD
print(ans[H][W])