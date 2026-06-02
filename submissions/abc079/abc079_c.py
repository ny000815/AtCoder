nums = list(map(int, list(input())))
ALL = 8
for i in range(ALL):
  ops = []
  su = nums[0]
  for j in range(3):
    if i & (1<<j):
      su += nums[j+1]
      ops.append('+')
    else:
      su -= nums[j+1]
      ops.append('-')
  if su == 7:
    break

print(nums[0], ops[0], nums[1], ops[1], nums[2], ops[2], nums[3], "=7", sep = "")