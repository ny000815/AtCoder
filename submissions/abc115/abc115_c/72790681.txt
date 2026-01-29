H = []
N, K = map(int, input().split())
for i in range(N):
  H.append(int(input()))

H.sort()
res = 10 ** 10
for i in range(K - 1, N):
  ans = H[i] - H[i - K +1]
  if ans < res:
    res = ans
print(res)