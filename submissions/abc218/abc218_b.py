nums = list(map(int, input().split()))

# a  6925
res = ""
for i in range(26):
  res += chr(nums[i] + ord("a") - 1)

print(res)