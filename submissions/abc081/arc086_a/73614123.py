N, K = map(int, input().split())
A = list(map(int, input().split()))
INT_MAX = 10 ** 100
numsSet = set()
nums = [INT_MAX] * (N + 1)

for i in range(N):
  numsSet.add(A[i])
  if nums[A[i]] == INT_MAX:
    nums[A[i]] = 1
  else:
    nums[A[i]] += 1
#print(numsSet)
nums.sort()
#print(nums)
ans = 0
cnt = 0
while len(numsSet) - cnt > K:
  ans += nums[0+cnt]
  #print(nums.index(min(nums)))
  cnt += 1
print(ans)