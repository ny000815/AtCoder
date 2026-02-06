H, W = map(int, input().split())
S = [input() for _ in range(H)]

ZX = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
ZY = [1, 0, -1, 1, 0, -1, 1, 0, -1]
res = [[0] * W for _ in range(H)]


for i in range(H):
  for j in range(W):
    for zx, zy in zip(ZX, ZY):
      ni, nj = i + zx, j + zy
      if ni < 0 or nj < 0 or ni >= H or nj >= W:
        continue
      if S[ni][nj] == '#':
        res[i][j] += 1

for i in range(H):
  for j in range(W):
    print(res[i][j], end = "")
  print("")