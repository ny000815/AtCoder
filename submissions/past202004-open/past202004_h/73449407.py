
N, M = map(int, input().split())
A = []
for _ in range(N):
  s = input()
  A.append(s)

groups = []
for n in range(11):
  groups.append([])

for i in range(N):
  for j in range(M):
    if A[i][j] == 'S':
      group = 0
    elif A[i][j] == 'G':
      group = 10
    else:
      group = int(A[i][j])
    groups[group].append([i, j])

dist = []
for n in range(N):
  dist.append([])
INF = 10 ** 100
for i in range(N):
  for j in range(M):
    dist[i].append(INF)
dist[groups[0][0][0]][groups[0][0][1]] = 0

for n in range(1, 11):
  for i, j in groups[n]:
    for i2, j2 in groups[n - 1]:
      dist[i][j] = min(dist[i][j], dist[i2][j2]+ abs(i - i2) + abs(j - j2))
  

gi, gj = groups[10][0]
if dist[gi][gj] == INF:
  print(-1)
else:
  print(dist[gi][gj])
