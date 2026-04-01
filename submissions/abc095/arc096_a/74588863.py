A, B, C, X, Y = map(int, input().split())
ans = 10**1000
for n in range(0, 2 * max(X, Y) + 1, 2):
  sm = C * n
  a = X - n // 2
  b = Y - n // 2
  if a > 0:
    sm += A*a
  if b > 0:
    sm += B*b
  ans = min(ans, sm)
print(ans)