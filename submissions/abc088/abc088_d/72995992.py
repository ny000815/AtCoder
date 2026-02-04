from queue import Queue
H, W = map(int, input().split())
S = [input() for _ in range(H)]
que = Queue()

DX = [1, -1, 0, 0]
DY = [0, 0, -1, 1]

dist = [[-1] * W for _ in range(H)]
dist[0][0] = 0
que.put((0,0))

while not que.empty():
  i, j = que.get()
  for dx, dy in zip(DX, DY):
    ni, nj = dx + i, dy + j
    if ni < 0 or ni >= H or nj < 0 or nj >= W:
      continue
    if S[ni][nj] == "#":
      continue
    if dist[ni][nj] != -1:
      continue
    dist[ni][nj] = dist[i][j] + 1
    que.put((ni, nj ))

blank = (sum(line.count(".") for line in S))
if dist[H - 1][W - 1] != -1:
  print(blank - dist[H-1][W-1] - 1)
else:
  print(-1)