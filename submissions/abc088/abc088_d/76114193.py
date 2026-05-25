from queue import Queue
H, W = map(int, input().split())
grid = []
for i in range(H):
    grid.append(input())
visited = [[-1] * W for _ in range(H)]
visited[0][0] = 1
que = Queue()
que.put((0, 0))

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

while not que.empty():
    x, y = que.get()
    for dx, dy in zip(DX, DY):
        nx, ny = x + dx, y + dy
        if 0 > nx or nx >= H or 0 > ny or ny >= W:
            continue
        if visited[nx][ny] != -1:
            continue
        if grid[nx][ny] == '#':
            continue
        visited[nx][ny] = visited[x][y] + 1
        que.put((nx, ny))

cnt = 0
for i in range(H):
    for j in range(W):
        cnt += 1 if grid[i][j] == '.' else 0
print(cnt - visited[H-1][W-1] if visited[H-1][W-1] != -1 else -1)