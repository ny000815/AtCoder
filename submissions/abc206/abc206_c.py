from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
nums = defaultdict(int)
for i in range(N):
  nums[A[i]] += 1

minus = 0
for n in nums:
  minus += (nums[n] * (nums[n]-1)) // 2
default = (N * (N -1)) // 2
print(default - minus)