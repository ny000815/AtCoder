from queue import Queue

N, M = map(int, input().split())
route = [[]for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    route[A].append(B)
    route[B].append(A)
visited = [-1] * (N+1)
visited[1] = 0
que = Queue()
que.put(1)
while not que.empty():
    curr = que.get()
    nextnodes = route[curr]
    for node in nextnodes:
        if visited[node] == -1:
            visited[node] = curr
            que.put(node)
if not -1 in visited[1:]:
    print("Yes")
    for i in range(2, N+1):
        print(visited[i])
else:
    print("No")

