s = input()
hasC = False
hasF = False
for i in range(len(s)):
  if s[i] == 'C':
    hasC = True
  if hasC and s[i] == 'F':
    hasF = True

print("Yes" if hasF else "No")