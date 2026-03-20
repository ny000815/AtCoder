N, M = map(int, input().split())

for i in range(N):
  print("Too Many Requests" if i >= M else "OK")