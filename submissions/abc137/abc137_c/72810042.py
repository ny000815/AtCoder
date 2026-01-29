from collections import defaultdict
S = defaultdict(int)
N = int(input())
for _ in range(N):
  S["".join(sorted(input()))] += 1
res = 0
for n in S:
  res += S[n] * (S[n] - 1) // 2
print(res)