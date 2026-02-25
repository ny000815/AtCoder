N = int(input())
strings = []
for _ in range(N):
  strings.append(input())

nums = []
for i in range(N):
  abcList = [0] * 26
  for c in strings[i]:
    abcList[ord(c) - ord('a')] += 1
  nums.append(abcList)

ans = ""
for i in range(26):
  minN = nums[0][i]
  for j in range(N):
    if minN > nums[j][i]:
      minN = nums[j][i]
  ans += chr(i + ord('a')) * minN
print(ans)