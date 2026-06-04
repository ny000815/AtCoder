from collections import deque
DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

H, W, N = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

pos = [None] * (N + 1)

for i in range(H):
    for j in range(W):
        if S[i][j] == 'S':
            pos[0] = (i, j)
        elif S[i][j].isdigit():
            pos[int(S[i][j])] = (i, j)


def bfs(a, b, gx, gy):
    que = deque()
    visited = [[-1]*W for _ in range(H)]
    visited[a][b] = 0
    que.append((a, b))
    while que:
        x, y = que.popleft()
        for dx, dy in zip(DX, DY):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if S[nx][ny] == 'X':
                continue
            if visited[nx][ny] != -1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            if nx == gx and ny == gy:
                return visited[nx][ny]
            que.append((nx, ny))


ans = 0
for i in range(N):
    a, b = pos[i]
    gx, gy = pos[i+1]
    ans += bfs(a, b, gx, gy)

print(ans)