N, M, X = map(int, input().split())
A, C = [],[]
for i in range(N):
    tmp = list(map(int, input().split()))
    C.append(tmp[0])
    A.append(tmp[1:])
INF = 10 ** 9 + 1
ans = INF

for bit in range(1<<N):
    totalCost = 0
    status = [0] * M
    for i in range(N):
        if bit & (1 << i):
            totalCost += C[i]
            for j in range(M):
                status[j] += A[i][j]
    isOk = True
    for k in range(M):
        if status[k] < X:
            isOk = False
            break
    if isOk:
        ans = min(ans, totalCost)
print(ans if ans != INF else -1)
