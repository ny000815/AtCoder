N = int(input())
S = input()

ans = 0
for i in range(N):
  x = S[:i]
  y = S[i:]
  xs = set(x)
  xy = set(y)
  ans = max(ans, len(xs & xy))

print(ans)