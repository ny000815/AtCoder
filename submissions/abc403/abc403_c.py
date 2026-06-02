N, M, Q = map(int, input().split())
users = [set() for _ in range(N)]

flagAll = [False]*N
for _ in range(Q):
  q, X, *Y = map(int, input().split())
  X -= 1
  if q == 1:
    users[X].add(Y[0])
  elif q == 2:
    flagAll[X] = True
  elif q == 3:
    if flagAll[X] or Y[0] in users[X]:
      print("Yes")
    else:
      print("No")