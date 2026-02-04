S = input()
T = input()
temp = ""
isRotation = False

for i in range(0, len(S)):
  swapped = (S[i:] + S[0:i]) 
  if swapped == T:
    isRotation = True
if isRotation:
  print("Yes")
else:
  print("No")