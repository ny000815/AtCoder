N = int(input())
isValid = True
used = set()
for i in range(N):
  W = input()
  if i == 0:
    next = W[-1]
    used.add(W)
  else:
    if W[0] != next or W in used:
      isValid = False
    used.add(W)
    next = W[-1]
print("Yes"  if isValid else "No")