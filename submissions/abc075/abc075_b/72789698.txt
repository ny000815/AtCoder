DX = [0, 0, 1, 1, 1, -1, -1, -1]
DY = [1, -1, 0, 1, -1, 0, 1, -1]
H, W = map(int, input().split())
S = [input() for i in range(H)]

result = [[0 if v == '.' else '#' for v in row] for row in S]
for i in range(H):
  for j in range(W):
    for dx, dy in zip(DX, DY):
      if result[i][j] == '#':
        continue
      ni, nj = i + dx, j + dy
      if ni >= H or ni < 0 or nj >= W or nj < 0:
        continue
      if result[ni][nj] == '#':
        result[i][j] += 1
      
for row in result:
  print(*row, sep = "")