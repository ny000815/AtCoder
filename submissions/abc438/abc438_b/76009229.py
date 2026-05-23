N, M = map(int, input().split())
S = input()
T = input()

def calcDiff (A, B):
    if A >= B:
        return A - B
    else:
        return 10 - B + A
ans = 10 ** 100
for i in range(N-M+1):
    cnt = 0
    for j in range(M):
        cnt += calcDiff(int(S[i+j]), int(T[j]))
    ans = min(ans, cnt)
print(ans)