from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

prefixSum = 0
cnt = defaultdict(int)
cnt[0] = 1
ans = 0
for a in A:
  prefixSum += a
  ans += cnt[prefixSum]
  cnt[prefixSum] += 1
print(ans)