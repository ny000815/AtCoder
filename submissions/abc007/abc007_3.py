from collections import deque
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [input() for _ in range(R)]
dist = [[-1] * C for _ in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

qeue = deque()
qeue.append([sy, sx])
dist[sy][sx] = 0

while qeue:
  y, x = qeue.popleft()
  for ny, nx in [[y + 1, x], [y, x + 1], [y - 1, x], [y, x - 1]]:
    if not (0 <= ny < R and 0 <= nx < C):
      continue
    if c[ny][nx] == '#':
      continue
    if dist[ny][nx] == -1:
      dist[ny][nx] = dist[y][x] + 1
      qeue.append([ny, nx])

print(dist[gy][gx])