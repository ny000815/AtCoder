N = int(input())
A = list(map(int, input().split()))
A.sort()
pList = []
for i in range(1, N+1):
  pList.append(i)
if pList == A:
  print("Yes")
else:
  print("No")