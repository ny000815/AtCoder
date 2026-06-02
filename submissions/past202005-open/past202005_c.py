A, R, N = map(int, input().split())
isLarge = False
value = A
if R == 1:
  pass
else:
  for i in range(1,N):
    value *= R
    if value > 1000000000:
      isLarge = True
      break;
print(value if not isLarge else "large")