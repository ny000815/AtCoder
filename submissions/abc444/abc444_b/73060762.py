N, K= map(int, (input().split()))
res = 0

for i in range(1, N+1):
  nums = []
  while i > 0:
    nums.append(i % 10)
    i //= 10
  sum = 0
  for num in nums:
    sum += num
  if sum == K:
    res += 1
print(res)
