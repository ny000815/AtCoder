A, B = map(int, input().split())
cnt = 0
for i in range(A, B+1):
  numlist = []
  while i > 0:
    numlist.append(i % 10)
    i //= 10
  if numlist[0] == numlist[4] and numlist[1] == numlist[3]:
    cnt += 1
print(cnt)
