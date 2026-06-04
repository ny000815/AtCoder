import sys
sys.setrecursionlimit(200000)
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

visited = [-1] * (N + 1)
def dfs(graph, start, visited):
    visited[start] = 1
    for next in graph[start]:
        if visited[next] == -1:
            dfs(graph, next, visited)
    return

dfs(graph, 1, visited)
visited = visited[1:]
print("The graph is connected." if not -1 in visited else "The graph is not connected.")

