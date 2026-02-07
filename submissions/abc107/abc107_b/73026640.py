H, W = map(int, input().split())
S = [input() for _ in range(H)]


row = [i for i in range(H) if '#' in S[i]]

column = []
for j in range(W):
  hasHash = False
  for i in range(H):
    if S[i][j] == '#':
      hasHash = True
      break
  if hasHash:
    column.append(j)

for i in row:
  for j in column:
    print(S[i][j], end = "")
  print("")