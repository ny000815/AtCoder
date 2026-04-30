A, B, C = input().split()
B = int(B)
C = int(C)
a = int(A[-1])

if a == 0:
  loop = [0,0,0,0]
if a == 1:
  loop = [1, 1, 1, 1]
if a == 2:
  loop = [2, 4, 8, 6]
if a == 3:
  loop = [3, 9, 7, 1]
if a == 4:
  loop = [4, 6, 4, 6]
if a == 5:
  loop = [5, 5, 5, 5]
if a == 6:
  loop = [6, 6, 6, 6]
if a == 7:
  loop = [7, 9, 3, 1]
if a == 8:
  loop = [8, 4, 2, 6]
if a == 9:
  loop = [9, 1, 9, 1]

if B % 4 == 0:
  div = 0
if B % 4 == 1:
  div = 1
if B % 4 == 2:
  div = 0
if B % 4 == 2 and C == 1:
  div = 2
if B % 4 == 3 and C % 2 == 0:
  div = 1
if B % 4 == 3 and C % 2 == 1:
  div = 3
if div == 0:
  div = 4
div -= 1
print(loop[div])
