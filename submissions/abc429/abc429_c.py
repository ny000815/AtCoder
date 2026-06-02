from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for i in range(N):
  d[A[i]] += 1
ans = 0
for n in d:
  if d[n] > 1:
    ans += d[n] * (d[n] - 1) // 2 * (N - d[n])
print(ans)