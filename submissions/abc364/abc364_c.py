N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cntA = 0
cuml = 0
A.sort(reverse = True)
for i in range(N):
  cntA += 1
  cuml += A[i]
  if cuml > X:
    break

cntB = 0
cuml = 0
B.sort(reverse = True)
for i in range(N):
  cntB += 1
  cuml += B[i]
  if cuml > Y:
    break
  
ans = min(cntA, cntB)
print(ans)