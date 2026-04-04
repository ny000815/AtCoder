N = int(input())
a = []
for i in range(N):
  a.append(int(input())-1)
curr = 0
cnt = 0
reached2 = False
for i in range(N):
  curr = a[curr]
  cnt += 1
  if curr == 1:
    reached2 = True
    break
print(cnt if reached2 else -1)