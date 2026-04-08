N = int(input())
S = [0]
for _ in range(N):
  S.append(input())
X, Y = input().split()
if S[int(X)] == Y:
  print("Yes")
else:
  print("No")