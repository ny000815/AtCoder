
A = []
zx = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
zy = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2, 2, 1, 0]

for i in range(3):
  A.append(list(map(int, input().split())))
N = int(input())
b = [0] * N
for i in range(N):
  b[i] = (int(input()))
for i in range(N):
  for j in range(3):
    for k in range(3):
      if b[i] == A[j][k]:
        A[j][k] = -1

isBingo = False
for i in range(8):
  a = zx.pop(0)
  b = zy.pop(0)
  c = zx.pop(0)
  d = zy.pop(0)
  e = zx.pop(0)
  f = zy.pop(0)
  if A[a][b] == -1 and A[c][d] == -1 and A[e][f] == -1:
    isBingo = True

print("Yes" if isBingo else "No")
