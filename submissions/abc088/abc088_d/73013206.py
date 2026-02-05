from queue import Queue
H, W = map(int, input().split())
s = [input() for i in range(H)]
DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]

que = Queue()
que.put((0,0))
dist = [[-1] * W for _ in range (H)] 
dist [0][0] = 0

while not que.empty():
  i, j = que.get()
  for zi, zj in zip(DX, DY):
    ni, nj = zi + i, zj + j
    if ni < 0 or nj < 0 or ni >= H or nj >= W:
      continue
    if s[ni][nj] == '#':
      continue
    if dist[ni][nj] != -1:
      continue
    que.put((ni, nj))
    dist[ni][nj] = dist[i][j] + 1

white = sum(list.count(".") for list in s)
if dist[H - 1][W - 1] != -1:
  print(white -dist[H - 1][W - 1] - 1)
else:
  print(-1)