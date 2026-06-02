X, Y = map(int, input().split())

ans = 0
i = X
while i <= Y:
  ans += 1
  i *= 2

print(ans)