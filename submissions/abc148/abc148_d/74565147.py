N = int(input())
A = list(map(int, input().split()))


breakable = True
if not 1 in A:
  breakable = False
num = 1
for i in range(N):
  if A[i] == num:
    num += 1
print(N - num + 1 if breakable else -1)