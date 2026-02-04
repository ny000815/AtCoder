N = int(input())
isInMulTable = False
for i in range(0, 30):
  for j in range(0, 20):
    if i * 4 + j * 7 == N:
      isInMulTable = True
print("Yes" if isInMulTable else "No")