N = int(input())
isInMulTable = False
for i in range(1, 10):
  for j in range(1, 10):
    if i * j == N:
      isInMulTable = True
print("Yes" if isInMulTable else "No")