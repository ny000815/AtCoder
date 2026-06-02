X, C = map(int, input().split())
ans = 0
for i in range(X//1000):
  if i * C * 1000 / 1000 + i * 1000 <= X:
    ans = i * 1000
print(ans)