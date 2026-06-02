N = int(input())
nameDict = {}
for i in range(1, N + 1):
  S = input()
  if S in nameDict:
    nameDict[S] += 1
    continue
  else:
    nameDict[S] = 1
#print(nameDict)
maxnum = max(nameDict.values())
#print(max(nameDict.values()))
nameDict = dict(sorted(nameDict.items()))
for n in nameDict.keys():
  if nameDict[n] == maxnum:
    print(n)