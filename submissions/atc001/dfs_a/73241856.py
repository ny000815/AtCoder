import sys
sys.setrecursionlimit(1000000) 
H, W = map(int, input().split())
C = [input() for _ in range(H)]
res = [[False] * W for _ in range(H)]

for i in range(H):
  for j in range(W):
    if C[i][j] == 's':
      si, sj = i, j
    if C[i][j] == 'g':
      gi, gj = i, j

def dfs(i, j):
  res[i][j] = True
  for ni, nj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
    if not(0 <= ni < H and 0 <= nj < W):
      continue
    if C[ni][nj] == '#':
      continue
    if not res[ni][nj]:
      dfs(ni, nj)

dfs(si, sj)

print("Yes" if res[gi][gj] else "No")