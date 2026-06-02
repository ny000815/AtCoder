N = int(input())
A = list(map(int, input().split()))
allOddCount = 1
for i in range(N):
  if A[i] % 2 == 0:
    allOddCount *= 2
allCount = 1
for i in range(N):
  allCount *= 3
print(allCount- allOddCount)