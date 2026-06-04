H, W = map(int, input().split())
S =[]
for _ in range(H):
    S.append(input())

DX = [1, 0, 0, -1]
DY = [0, 1, -1, 0]

ans = 0
isValid = True
for i in range(H):
    for j in range(W):
        if S[i][j] != '#':
            continue
        cnt = 0
        for dx, dy in zip(DX, DY):
            ni, nj = i + dx, j + dy
            if ni <0 or ni >= H or nj < 0 or nj >= W:
                continue
            if S[ni][nj] == '#':
                cnt += 1
        if cnt != 2 and cnt != 4:
            isValid = False
print("Yes" if isValid else "No")
