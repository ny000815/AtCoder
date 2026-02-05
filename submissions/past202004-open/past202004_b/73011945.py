S = input()
cnta = S.count("a")
cntb = S.count("b")
cntc = S.count("c")
answer = max(cnta, cntb, cntc)
if answer == cnta:
  print("a")
elif answer == cntb:
  print("b")
elif answer == cntc:
  print("c")