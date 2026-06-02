standings = []
scores = list(map(int, input().split()))
scores = [-score for score in scores]
for bit in range(1, 32):
  score = 0
  name = ""
  for digit in range(5):
    if bit & 1 << digit:
      score += scores[digit]
      name += "ABCDE"[digit]
  standings.append((score, name))

for _, name in sorted(standings):
  print(name)