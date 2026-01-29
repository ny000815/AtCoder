N, K = map(int, input().split())
L = list(map(int, input().split()))
L.sort(reverse = True)
res = 0
for i in range(K):
  res += L[i]
print(res)