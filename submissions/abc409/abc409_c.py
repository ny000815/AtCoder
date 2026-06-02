N, L = map(int, input().split())
d = list(map(int, input().split()))
cord = [0] * L
curr = 0
cord[curr] += 1
for i in range(N-1):
  curr += d[i]
  curr %= L
  cord[curr] += 1
ans = 0
for i in range(L // 3):
  ans += cord[i] * (cord[i + L // 3] * cord[i + 2 * L // 3])
if L % 3 != 0:
  ans = 0
print(ans)