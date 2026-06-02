N = int(input())
S = input()
pos = [0, 0]
revisit = False
visited = set()
for i in range(N):
  visited.add((pos[0], pos[1]))
  if S[i] == 'R':
    pos[0] += 1
  elif S[i] == 'L':
    pos[0] -= 1
  elif S[i] == 'U':
    pos[1] += 1
  else:
    pos[1] -= 1
  if (pos[0], pos[1]) in visited:
    revisit = True
print("Yes" if revisit else "No")
