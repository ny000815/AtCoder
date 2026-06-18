from collections import defaultdict
S = input()
ok = True
if len(S) %2 != 0:
    ok = False

length = len(S)
for i in range(0, length-1,2):
    if S[i] != S[i + 1]:
        ok = False

alphaDict = defaultdict(int)
for i in range(length):
    alphaDict[S[i]] += 1
for k, v in alphaDict.items():
    if v == 2 or v == 0:
        continue
    ok = False

print("Yes" if ok else "No")