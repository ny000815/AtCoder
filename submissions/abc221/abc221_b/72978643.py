S = input()
T = input()
temp = ""
isTypo = False
if S == T:
  isTypo = True
for i in range(1, len(S)):
  swapped = (S[0:i - 1] + S[i]  + S[i - 1]  + S[i+1:]) 
  if swapped == T:
    isTypo = True
if isTypo:
  print("Yes")
else:
  print("No")