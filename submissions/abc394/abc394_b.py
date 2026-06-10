N = int(input())
S = []
for _ in range(N):
    s = (input())
    S.append([len(s), s])
S.sort()
for i in range(N):
    print(S[i][1], end = "")

print("")