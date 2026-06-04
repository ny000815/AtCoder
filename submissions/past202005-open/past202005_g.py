from collections import deque
DX = [1, 0, -1, 1, -1, 0]
DY = [1, 1, 1, 0, 0, -1]


OFFSET = 400
SIZE = 801

N, X, Y = map(int, input().split())
X += OFFSET
Y += OFFSET

grid = [[-1] * (SIZE) for _ in range(SIZE)]
for i in range(N):
    x, y = map(int, input().split())
    grid[x+OFFSET][y+OFFSET] = '#'


que = deque()
que.append((OFFSET, OFFSET))
grid[OFFSET][OFFSET] = 0
while que:
    x, y = que.popleft()
    for a, b in zip(DX, DY):
        nx, ny = x + a, y + b
        if 0 > nx or nx >= SIZE or 0 > ny or ny >= SIZE:
            continue
        if grid[nx][ny] != -1:
            continue
        if grid[nx][ny] == '#':
            continue
        grid[nx][ny] = grid[x][y]+1
        que.append((nx, ny))
        if nx == X and ny == Y:
            print(grid[nx][ny])
            exit()
print(-1)
