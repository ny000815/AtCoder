N = int(input())
A = list(map(int, input().split()))


A = sorted(A)
ans = []

isEven = len(A) % 2 == 0

isPerfect = True
if isEven:
  propLen = A[0] + A[len(A) - 1]
  for i in range(len(A) // 2):
    if A[i] + A[len(A) - 1 - i] != propLen:
      isPerfect = False
      
  if isPerfect:
    ans.append(propLen)

isPerfect = True
capLen = A[N - 1]
B = []
for n in A:
  if n < capLen:
    B.append(n)


doesExist = len(B)
if not doesExist:
  capLen = A[0]

if doesExist:
  if len(B) % 2 != 0:
    isPerfect = False
  for i in range(len(B) // 2):
    if B[i] + B[len(B) - 1 - i] != capLen:
      isPerfect = False

if isPerfect and capLen not in ans:
  ans.append(capLen)
ans.sort()
print(*ans)