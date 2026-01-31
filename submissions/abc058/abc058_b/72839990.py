O = input()
E = input()
res = ""
for i in range(len(O)):
  res += (O[i])
  if len(O) != len(E) and i == len(O) - 1:
    continue
  res += (E[i])
print(res)