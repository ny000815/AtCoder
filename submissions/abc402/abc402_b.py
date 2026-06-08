from collections import deque
Q = int(input())
line = deque()
for i in range(Q):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        line.append(temp[1])
    else:
        print(line.popleft())