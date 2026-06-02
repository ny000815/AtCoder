N, M = map(int, input().split())
S = input()
T = input()

ans = 10 ** 10
for i in range(N-M+1):
    cnt = 0
    for j in range(M):
        cnt += (int(S[i+j]) - int(T[j])) % 10
    ans = min(ans, cnt)
print(ans)