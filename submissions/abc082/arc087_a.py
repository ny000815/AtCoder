N = int(input())
numDict = {}
a = list(map(int, input().split()))
for i in range(N):
  if a[i] in numDict:
    numDict[a[i]] += 1
  else:
    numDict[a[i]] = 1
items = numDict.items()
ans = 0
for i, j in items:
  if i > j:
    ans += j
  elif i < j:
    ans += j - i
print(ans)