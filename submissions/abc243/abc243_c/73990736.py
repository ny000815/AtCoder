N = int(input())
A, B = [], []
points = [tuple(map(int, input().split())) for _ in range(N)]
S = input()
maxL, minR = {}, {}
for i in range(N):
  x, y = points[i]
  if S[i] == 'R':
    if not y in minR:
      minR[y] = x
    else:
      minR[y] = min(x, minR[y])
  else:
    if not y in maxL:
      maxL[y] = x
    else:
      maxL[y] = max(x, maxL[y])

hasCollisicon = False
for y in minR:
  if y in maxL and minR[y] <= maxL[y]:
    hasCollisicon = True
print("Yes" if hasCollisicon else "No")