def rec(N, X, P, B):
    if N == 0:
        return 1
    elif X == 1:
        return 0
    elif X <= B[N - 1] + 1:
        return rec(N - 1, X- 1, P, B)
    elif X == B[N - 1] + 2:
        return P[N - 1] + 1
    elif X < 2 * B[N - 1] + 3:
        return rec(N - 1, X - B[N - 1] - 2, P, B)+ P[N - 1] + 1
    else:
        return  P[N - 1] * 2 + 1



N, X = map(int, input().split())
P = [1] * (N + 1)
B = [1] * (N + 1)
for i in range(1, N + 1):
    P[i] = 2 * P[i - 1] + 1
    B[i] = 2 * B[i - 1] + 3
print(rec(N, X, P, B))