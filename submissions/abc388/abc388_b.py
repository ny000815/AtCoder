N, D = map(int, input().split())
T, L = [], []
for _ in range(N):
    t, l = map(int, input().split())
    T.append(t)
    L.append(l)
for i in range(1, D+1):
    ans = 0
    for j in range(len(T)):
        ans = max(ans, T[j] * (L[j]+ i))
    print(ans)