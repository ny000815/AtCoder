N, C = map(int, input().split())
T = list(map(int, input().split()))
ans = 1
lastGiven = T[0]
for i in range(1,N):
    if T[i] - lastGiven >= C:
        ans += 1
        lastGiven = T[i]
print(ans)