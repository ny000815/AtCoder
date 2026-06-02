N = int(input())
A = list(map(int, input().split()))
numsDict = {}
for i in range(N):
  if not A[i] in numsDict:
    numsDict[A[i]] = i
    print(-1, end = " ")
  else:
    print(numsDict[A[i]] + 1, end = " ")
    numsDict[A[i]] = i