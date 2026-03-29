H, W, N = map(int, input().split())
A = []
for _ in range(H):
  A.append(list(map(int, input().split())))
B = []
ans = [0] * H
for i in range(N):
  B.append(int(input()))
  for i in range(H):
    for j in range(W):
      if A[i][j] == B[-1]:
        ans[i] += 1
print(max(ans))
