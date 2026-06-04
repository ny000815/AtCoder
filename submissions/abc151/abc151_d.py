from collections import deque
H, W = map(int, input().split())
S =[]
for i in range(H):
    S.append(input())
maximum = 0

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        que = deque()
        que.append((i,j))
        visited = [[-1] * W for _ in range(H)]
        visited[i][j] = 0

        while que:
            a,b = que.popleft()
            for x, y in zip(DX, DY):
                na, nb = a+x, b+y
                if na >= H or na <0 or nb >= W or nb <0:
                    continue
                if visited[na][nb] != -1:
                    continue
                if S[na][nb] == '#':
                    continue
                visited[na][nb] = visited[a][b] + 1
                que.append((na,nb))
                if visited[na][nb] > maximum:
                    maximum = visited[na][nb]
print(maximum)