H, W = map(int, input().split())
S = []
S = [list(input()) for _ in range(H)]
DX = [0,0,1,1,1,-1,-1,-1]
DY = [1,-1,0,1,-1,0,1,-1]

def dfs(x, y, S):
  S[x][y] = '.'
  stack = [(x, y)]
  while stack:
    x, y = stack.pop()
    for dx, dy in zip(DX, DY):
      nx = x + dx
      ny = y + dy
      if nx < 0 or ny < 0 or nx >= H or ny >= W:
        continue
      if S[nx][ny] == '#':
        S[nx][ny] = '.'
        stack.append((nx, ny))

cnt = 0
for i in range(H):
  for j in range(W):
    if S[i][j] == '#':
      cnt += 1
      dfs(i, j, S)
    
print(cnt)