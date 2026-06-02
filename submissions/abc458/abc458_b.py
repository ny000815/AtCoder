H, W = map(int, input().split())
data = [[0 for i in range(50)] for j in range(50)]

for i in range(H):
  for j in range(W):
    if i - 1 >= 0:
      data[i][j] += 1
    if i + 1 < H:
      data[i][j] += 1
    if j - 1 >= 0:
      data[i][j] += 1
    if j + 1 < W:
      data[i][j] += 1
    print(data[i][j], end = " ")
  print("")
