H = int(input())
W = 2*H - 1
S = [input() for _ in range(H)]

ZX = [1, 1, 1]
ZY = [1, 0, -1]
res = [["."] * W for _ in range(H)]
res[H-1] = list(S[H-1])


for i in range(H - 2, -1, -1):
  for j in range(W - 1, -1, -1):
    if S[i][j] == '.':
      continue
    res[i][j] = S[i][j]
    for zx, zy in zip(ZX, ZY):
      ni, nj = i + zx, j + zy
      if ni < 0 or nj < 0 or ni >= H or nj >= W:
        continue
      if res[ni][nj] == 'X':
        res[i][j] = 'X'
        continue
        
for i in range(H):
  for j in range(W):
    print(res[i][j], end = "")
  print("")