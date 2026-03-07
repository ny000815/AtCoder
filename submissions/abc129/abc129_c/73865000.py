N, M = map(int, input().split())
obs = [False] * (N + 1)
ans = [0] * (N + 1)

for _ in range(M):
  a = int(input())
  obs[a] = True

ans[0] = 1
MOD = 1000000007
for i in range(1, N+1):
  if obs[i]:
    continue
  if i == 1:
    ans[i] = ans[i - 1] % MOD
  else:
    ans[i] = (ans[i - 1] + ans[i - 2]) % MOD

print(ans[N])