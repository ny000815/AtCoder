N = int(input())
cSum1 = [0]
cSum2 = [0]
for i in range(1, N+1):
  C, P = map(int, input().split())
  cSum1.append(cSum1[i - 1])
  cSum2.append(cSum2[i - 1])
  if C == 1:
    cSum1[i] += P
  else:
    cSum2[i] += P


Q = int(input())
for i in range(Q):
  L, R = map(int, input().split())
  print(cSum1[R] - cSum1[L - 1], end = " ")
  print(cSum2[R] - cSum2[L - 1])
