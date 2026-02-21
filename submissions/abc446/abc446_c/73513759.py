from collections import deque
T = int(input())
for i in range(T):
  eggs = deque()
  N, D = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  for i in range(N):
    for _ in range(A[i]):
      eggs.append(i)
    for _ in range(B[i]):
      eggs.popleft()
    if len(eggs) > 0:
      while eggs[0] == i - D:
        eggs.popleft()
  print(len(eggs))