N = int(input())
ans = 0
for a in range(1,1000000):
  ans += (N - 1)//a
print(ans)