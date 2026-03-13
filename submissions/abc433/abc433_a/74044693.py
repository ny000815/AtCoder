X, Y, Z = map(int, input().split())
isMultiple = False
for i in range(1001):
  if X+i == (Y+i) * Z:
    isMultiple = True
print("Yes" if isMultiple else "No")