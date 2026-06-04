from collections import deque

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

visitable = 0
for i in range(N):
    for j in range(M):
        if S[i][j] == '.':
            visitable += 1


ans = 0
for i in range(N):
    for j in range(M):
        if S[i][j] == '.':
            continue
        grid = [[-1] * M for _ in range(N)]
        visited = 1
        que = deque()
        que.append((i, j))
        grid[i][j] = 1
        while que:
            x, y = que.popleft()
            for dx, dy in zip(DX, DY):
                nx, ny = x + dx, y + dy
                if 0 > nx or nx >= N or 0 > ny or ny >= M:
                    continue
                if S[nx][ny] == '#' and not (nx == i and ny == j):
                    continue
                if grid[nx][ny] != -1:
                    continue
                grid[nx][ny] = 1
                visited += 1
                que.append((nx, ny))
        if visited == visitable+1:
            ans += 1

print(ans)
