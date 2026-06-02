def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

N = int(input())
A = list(map(int, input().split()))
prefix = [0] * (N + 1)
prefix[1] = A[0]
for i in range(1, N):
  prefix[i + 1] = gcd(A[i], prefix[i])

suffix = [0] * (N + 1)
suffix[N-1] = A[N-1]
for i in range(N-2, -1, -1):
  suffix[i] = gcd(A[i], suffix[i+1])

ans = 0
for i in range(N):
  ans = max(ans, gcd(prefix[i], suffix[i + 1]))
print(ans)