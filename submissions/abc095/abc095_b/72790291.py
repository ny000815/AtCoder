M = []
N, X = map(int, input().split())
for i in range(N):
  M.append(int(input()))
M.sort()
cnt = N
rest = X - sum(M)
if rest // M[0] > 0:
  cnt += rest // M[0]
print(cnt)