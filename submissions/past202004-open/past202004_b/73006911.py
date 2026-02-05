S = input()
cntA = S.count("a")
cntB = S.count("b")
cntC = S.count("c")
if cntA < cntB:
  if cntB < cntC:
    print("c")
  else:
    print("b")
else:
  if cntA < cntC:
    print("c")
  else:
    print("a")