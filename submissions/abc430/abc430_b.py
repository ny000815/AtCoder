N, M = map(int, input().split())
S = []
for i in range(N):
    S.append(input())
pattern = set()
for i in range(N - M + 1):
    for j in range(N - M + 1):
        subgrid = []
        for a in range(M):
            subgrid.append(S[i+a][j:j + M])
        pattern.add("".join(subgrid))
print(len(pattern))
