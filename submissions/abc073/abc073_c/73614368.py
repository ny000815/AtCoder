N = int(input())
numSet = set()
for _ in range(N):
  A = int(input())
  if A in numSet:
    numSet.remove(A)
  else:
    numSet.add(A)
print(len(numSet))