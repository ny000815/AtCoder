nums = list(map(int, input().split()))
nums.sort(reverse = True)
for i in range(3):
  print(nums[i],end = "")