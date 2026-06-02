N = int(input())
if N % 2 == 0:
  for i in range(1, N+1):
    if i == N // 2 or i == N // 2 + 1:
      print("=",end = "")
    else:
      print('-',end = "")
else:
  for i in range(1, N+1):
    if i == N // 2 + 1:
      print("=",end = "")
    else:
      print('-',end = "")