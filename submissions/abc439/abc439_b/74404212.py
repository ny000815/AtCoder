N = int(input())

for i in range(300):
  ans = 0
  while N > 0:
    ans += (N % 10)**2
    N //= 10
  N = ans
print("Yes" if N == 1 else "No")