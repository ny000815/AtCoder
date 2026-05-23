H, W, K = map(int, input().split())
c = []
for i in range(H):
    c.append(input())
ans = 0

for mskH in range(1 << H):
    for mskW in range(1 << W):
        cnt = 0
        for h in range(H):
            for w in range(W):
                if mskH & (1 << h) or mskW & (1 << w):
                    continue
                if c[h][w] == '#':
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)
