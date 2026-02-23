Q = int(input())
vol = 0
isPlayed = False
for _ in range(Q):
  A = int(input())
  if A == 1:
    vol += 1
  elif A == 2:
    if vol >=1:
      vol -= 1
  elif A == 3:
    if isPlayed:
      isPlayed = False
    else:
      isPlayed = True
  if vol >= 3 and isPlayed:
    print("Yes")
  else:
    print("No")