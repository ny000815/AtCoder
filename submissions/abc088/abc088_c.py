c = [list(map(int, input().split())) for _ in range(3)]
b1mb2 = c[0][0] - c[0][1]
b2mb3 = c[0][1] - c[0][2]
isValid = True
for i in range(1,3):
  if b1mb2 != c[i][0] - c[i][1] or b2mb3 != c[i][1] - c[i][2]:
    isValid = False 
print("Yes" if isValid else "No")