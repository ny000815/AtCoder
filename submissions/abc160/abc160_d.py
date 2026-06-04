from collections import deque

N, X, Y = map(int, input().split())
route = [[i-1, i+1] for i in range(N+1)]
route[1] = [2]
route[N] = [N-1]
route[X].append(Y)
route[Y].append(X)

dist = [[-1] * (N + 1) for _ in range(N+1)]

for start in range(1, N+1):
    que = deque()
    que.append(start)
    dist[start][start] = 0
    while que:
        cur = que.popleft()
        for next in route[cur]:
            if dist[start][next] == -1:
                dist[start][next] = dist[start][cur] + 1
                que.append(next)
ans = [0] * (N+1)
for x in range(1, N+1):
    for y in range(x+1, N+1):
        ans[dist[x][y]] += 1
for i in range(1, N):
    print(ans[i])