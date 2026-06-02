N = int(input())
ans = 0
for i in range(1, N+1):
  if i % 2 == 0:
    ans += i ** 3
  else:
    ans += -i ** 3
print(ans)