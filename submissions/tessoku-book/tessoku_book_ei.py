import sys
sys.setrecursionlimit(200000)
from _collections import deque
N, M = map(int, input().split())
graph = [[]for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def dfs(prev, node, visited):
    visited[node] = prev
    for next in graph[node]:
        if not visited[next]:
            dfs(node, next, visited)
dfs(0, 1, visited)

path = deque()
n = visited[N]
path.append(N)
while n != 1:
    path.appendleft(n)
    n = visited[n]
path.appendleft(1)
print(*path)




