N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

order = {}

def dfs(current, used):
  if len(current) == N:
    order[tuple(current)] = len(order) + 1
    return
  
  for x in range(1, N+1):
    if not used[x]:
      current.append(x)
      used[x] = True
      
      dfs(current, used)
      
      current.pop()
      used[x] = False

used = [False] * (N+1)
dfs([], used)
print(abs(order[P] - order[Q]))