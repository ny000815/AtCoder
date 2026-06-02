S = input()
cntList = [0] * 27
for i in range(len(S)):
  cntList[ord(S[i]) - ord('a')] += 1
maxCnt = (max(cntList))
for i in range(len(S)):
  if cntList[ord(S[i]) - ord('a')] == maxCnt:
    continue
  else:
    print(S[i], end = "")

