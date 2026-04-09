N = int(input())
S = input()
if len(S) < 3:
  print("No")
else:
  print("Yes" if S[-3] == 't' and S[-2] == 'e' and S[-1] == 'a' else "No")