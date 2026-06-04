from collections import deque

DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]

H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(input())

que = deque()
visited = [[-1]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            que.append((i, j))
            visited[i][j] = 0

cnt = 0
while que:
    x, y = que.popleft()
    for dx, dy in zip(DX, DY):
        nx, ny = x + dx, y + dy
        if nx <0 or nx >= H or ny <0 or ny >= W:
            continue
        if visited[nx][ny] != -1:
            continue
        visited[nx][ny] = visited[x][y] + 1
        if visited[nx][ny] > cnt:
            cnt = visited[nx][ny]
        que.append((nx, ny))

print(cnt)
