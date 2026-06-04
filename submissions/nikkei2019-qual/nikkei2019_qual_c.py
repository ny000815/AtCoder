N = int(input())
scores = []
for _ in range(N):
    A, B = map(int, input().split())
    scores.append([A+B, A, B])
scores.sort(reverse=True)
scoreA = 0
scoreB = 0
i = 0
while i < N:
    scoreA += scores[i][1]
    if i < N-1:
        scoreB += scores[i+1][2]
        i += 1
    i += 1
print(scoreA - scoreB)
