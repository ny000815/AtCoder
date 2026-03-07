N, Q = map(int, input().split())
A = list(map(int, input().split()))
AS = sorted(A)
#print(AS)

for i in range(Q):
  K = int(input())
  B = list(map(int, input().split()))
  NGNum = dict()
  for i in range(K):
    if A[B[i] - 1] in NGNum:
      NGNum[A[B[i] - 1]] += 1
    else: 
      NGNum[A[B[i] - 1]] = 1
  j = 0
  #print(NGNum)
  while AS[j] in NGNum and NGNum[AS[j]] >= 1:
      NGNum[AS[j]] -= 1
      j += 1
  print((AS[j]))
  #print(NGNum)
  #print("")