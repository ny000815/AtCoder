N, M, T = map(int, input().split())
A = list(map(int, input().split()))
X = set()
Y = [0] * N
for i in range(M):
  x, y = map(int, input().split())
  X.add(x - 1)
  Y[x - 1] = y

canGoal = True
hp = T
for i in range(N-1):
  #print(i, hp, A[i])
  if hp > A[i] and canGoal:
    hp -= A[i]
    if i + 1 in X:
      hp += Y[i + 1]
  else:
    canGoal = False
  if hp <= 0:
    canGoal = False
print("Yes" if canGoal else "No")
