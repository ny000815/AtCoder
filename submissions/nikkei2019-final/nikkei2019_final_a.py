N = int(input())
A = list(map(int, input().split()))
for n in range(1,N+1):
  s = sum(A[:n])
  best = s
  for i in range(1,N - n + 1):
    s = s - A[i - 1] + A[i + n - 1]
    if s > best:
      best = s
  print(best)