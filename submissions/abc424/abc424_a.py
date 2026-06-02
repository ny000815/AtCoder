A, B, C = map(int, input().split())
isIsosceles = False
if A == B or B == C or A == C:
  isIsosceles = True
print("Yes" if isIsosceles else "No")