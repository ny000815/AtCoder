N = int(input())
T = input()
A = input()
isSame = False
for i in range(N):
  if T[i] == 'o' and A[i] == 'o':
    isSame = True
print("Yes" if isSame else "No")