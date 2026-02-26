N = int(input())
nameSet = set()
for i in range(1, N + 1):
  S = input()
  if S in nameSet:
    continue
  else:
    nameSet.add(S)
    print(i)