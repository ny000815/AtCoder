N, M = map(int, input().split())
S = []
for i in range(N):
    s = input()
    S.append(s)
scores = [0] * N
for i in range(M):
    countOne = 0
    for j in range(N):
        if S[j][i] == '1':
            countOne += 1
    if countOne > N / 2:
        for k in range(N):
            if S[k][i] == '0':
                scores[k] += 1
    else:
        for k in range(N):
            if S[k][i] == '1':
                scores[k] += 1
maxScore = max(scores)
ans = []
for i in range(N):
    if scores[i] == maxScore:
        ans.append(i+1)
print(*ans)

