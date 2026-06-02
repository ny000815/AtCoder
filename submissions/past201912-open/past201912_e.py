N, Q = map(int, input().split())
graph = [[False] * N for _ in range(N)]


for _ in range(Q):
  query = list(map(int, input().split()))
  query[1] -= 1
  
  if query[0] == 1:
    query[2] -= 1
    graph[query[1]][query[2]] = True
    
  if query[0] == 2:
    for i in range(N):
      if graph[i][query[1]]:
        graph[query[1]][i] = True
  
  if query[0] == 3:
    toFollow = []
    for i in range(N):
      if graph[query[1]][i]:
        for j in range(N):
          if graph[i][j] and j != query[1]:
            toFollow.append(j)
    for j in toFollow:
      graph[query[1]][j] = True

for i in range(N):
  for j in range(N):
    print("Y"if graph[i][j] else "N", end = "")
  print("")