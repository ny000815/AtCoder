nums = list(map(int, input().split()))
nums.sort()
print("Yes" if nums[0]+nums[1] == nums[2] or nums[0] == nums[1] == nums[2] else "No")