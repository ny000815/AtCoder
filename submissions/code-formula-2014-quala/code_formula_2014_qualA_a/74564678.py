A = int(input())
isSquare = False
for i in range(101):
  if i * i * i == A:
    isSquare = True
print("YES" if isSquare else "NO")