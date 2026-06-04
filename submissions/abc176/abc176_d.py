from collections import defaultdict, deque
DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

WX = [2, 2, 2, 2, 2, 1, 1, 0, 0, -1, -1, -2, -2, -2, -2, -2, 1, 1, -1, -1]
WY = [0, 1, 2, -1, -2, 2, -2, 2, -2, 2, -2, 0, 1, 2, -1, -2, 1, -1, 1, -1]

H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
Ch -=1; Cw -= 1; Dh -= 1; Dw -= 1

S = []
INF = float('inf')
for _ in range(H):
    S.append(input())
visited = [[INF]*W for _ in range(H)]
visited[Ch][Cw] = 0

que = deque()
que.append((Ch, Cw))

while que:
    x, y = que.popleft()
    for dx, dy in zip(DX, DY):
        nx, ny = x + dx, y + dy
        if 0 > nx or nx >= H or 0 > ny or ny >= W:
            continue
        if S[nx][ny] == '#':
            continue
        if visited[nx][ny] > visited[x][y]:
            visited[nx][ny] = visited[x][y]
            que.appendleft((nx, ny))
    for dx, dy in zip(WX, WY):
        nx, ny = x + dx, y + dy
        if 0 > nx or nx >= H or 0 > ny or ny >= W:
            continue
        if S[nx][ny] == '#':
            continue
        if visited[nx][ny] > visited[x][y] +1:
            visited[nx][ny] = visited[x][y] + 1
            que.append((nx, ny))
print(visited[Dh][Dw] if visited[Dh][Dw] != INF else -1)


