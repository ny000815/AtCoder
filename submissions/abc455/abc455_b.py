H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

ans = 0
for h1 in range(H):
    for h2 in range(h1,H):
        for w1 in range(W):
            for w2 in range(w1,W):
                isSymmetric = True
                for i in range(h1, h2 + 1):
                    for j in range(w1, w2 + 1):
                        if S[i][j] != S[h1+h2-i][w1+w2-j]:
                            isSymmetric = False
                if isSymmetric:
                    ans += 1
print(ans)

