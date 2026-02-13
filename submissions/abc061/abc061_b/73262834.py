N, M = map(int, input().split())

roads = [[0]*N for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  roads[a][b] += 1
  roads[b][a] += 1

for row in roads:
  print(sum(row))