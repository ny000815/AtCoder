N, M, X = map(int, input().split())
A, C = [],[]
for i in range(N):
    tmp = list(map(int, input().split()))
    C.append(tmp[0])
    A.append(tmp[1:])
INF = 10 ** 9 + 1
ans = INF

def dfs(i, cost, status):
    if i == N:
        if all(s >= X for s in status):
            return cost
        return INF
    res1 = dfs(i+1, cost, status)
    newStatus = status[:]
    for j in range(M):
        newStatus[j] += A[i][j]
    res2 = dfs(i+1, cost + C[i], newStatus)
    return min(res1, res2)
ans = dfs(0, 0, [0]*M)
print(ans if ans != INF else -1)

