m, n, N = map(int, input().split())

ans = N
while N >= m:
  q = N // m
  ans += q * n
  N = q * n + N % m
print(ans)