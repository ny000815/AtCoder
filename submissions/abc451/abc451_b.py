N, M = map(int, input().split())
cur = [0]*(M+1)
fut = [0]*(M+1)
for _ in range(N):
  A, B = map(int, input().split())
  cur[A] += 1
  fut[B] += 1
for i in range(1, M+1):
  print(fut[i]-cur[i])