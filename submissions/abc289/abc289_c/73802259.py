N, M = map(int, input().split())
lst = []
for i in range(M):
  q = int(input())
  nums = list(map(int, input().split()))
  lst.append(nums)

ans = 0
for b in range(1 << M):
  s = set()
  for i in range(M):
    if (b >> i) &1:
      s.update(lst[i])
  if len(s) == N:
    ans += 1

print(ans)