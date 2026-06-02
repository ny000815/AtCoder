N, Q = map(int, input().split())
L = [[] for _ in range(N)]
for i in range(N):
  L[i] = list(map(int, input().split()))
for _ in range(Q):
  S = list(map(int, input().split()))
  print(L[S[0]-1][S[1]])