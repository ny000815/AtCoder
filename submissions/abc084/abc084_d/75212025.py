def primeList(num):
  nums = [1] * 100001
  nums[0] = 0
  nums[1] = 0
  for i in range(2, int(num ** 0.5)):
    for j in range(i*i, num+1, i):
      nums[j] = 0
  return nums

num = 100000
primeNums = primeList(num)
numsLike2017 = [0] * num
for i in range(3, num, 2):
  if primeNums[(i+1)//2] and primeNums[i]:
    numsLike2017[i] = 1
  
prefixSum = [0] * num
for i in range(3, num):
  prefixSum[i] = prefixSum[i-1] + numsLike2017[i]

Q = int(input())
for i in range(Q):
  l, r = map(int, input().split())
  ans = prefixSum[r] - prefixSum[l-1]
  print(ans)

