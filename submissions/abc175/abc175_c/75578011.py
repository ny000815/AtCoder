X, K, D = map(int, input().split())
X = abs(X)
q = X // D
r = X % D
if K >= q:
  diff = K - q
  if diff % 2 == 0:
    ans = r
  else:
    ans = abs(r - D)
else:
  ans = X - K * D
print(ans)