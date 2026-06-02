N, M = map(int, input().split())
S = input()
T = input()
Q = int(input())
for i in range(Q):
  w = input()
  isTakahashi = True
  isAoki = True
  for i in range(len(w)):
    if not w[i] in S:
      isTakahashi = False
    if not w[i] in T:
      isAoki = False
  if isTakahashi and isAoki:
    print("Unknown")
  elif isTakahashi:
    print("Takahashi")
  else:
    print("Aoki")
