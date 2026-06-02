A, B = map(int, input().split())
S = input()
isLegit = True
if len(S) != A + B + 1:
  isLegit = False
for i in range(len(S)):
  if i == A:
    if S[i] != "-":
      isLegit = False
    continue
  if not '0' <= S[i] <= '9':
    isLegit = False
if isLegit:
  print("Yes")
else:
  print("No")