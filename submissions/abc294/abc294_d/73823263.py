from collections import deque
N, Q = map(int, input().split())
waiting = deque(i for i in range(1, N+1))
called = deque()
done = set()

for i in range(Q):
  args = input().split()
  qType = int(args[0])
  x = int(args[1]) if qType == 2 else 0 
  if qType == 1:
    called.append(waiting.popleft())
    #print(called)
    #print(waiting)
  if qType == 2:
    done.add(x)
  if qType == 3:
    while called and called[0] in done:
      called.popleft()
    print(called[0])