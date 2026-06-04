N, K = map(int, input().split())
L = [i for i in range(N + 1)]
dp = []
firstL = []
for i in range(N+1):
    subNum = 0
    num = L[i]
    while num > 0:
        subNum += num % 10
        num //= 10
    firstL.append(L[i] - subNum)
dp.append(firstL)

for d in range(1, 30):
    newRow = [0] * (N + 1)
    for i in range(N+1):
        newRow[i] = dp[d-1][dp[d-1][i]]
    dp.append(newRow)

indices = []
i = 0
while K > 0:
    if K & 1:
        indices.append(i)
    K >>= 1
    i += 1

for i in range(1, N+1):
    current = dp[indices[0]][i]
    for index in indices[1:]:
        current = dp[index][current]
    print(current)