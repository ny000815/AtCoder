X, Y = map(int, input().split())
xMulti = 1
isValid = False
for i in range(1, 1000):
  xMulti = X * i
  if xMulti % Y != 0:
    isValid = True
    break
print(xMulti if isValid else -1)