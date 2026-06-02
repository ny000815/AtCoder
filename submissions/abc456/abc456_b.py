A = []
for i in range(3):
  Ai = list(map(int, input().split()))
  A.append(Ai)
ans = 0
for i in A[0]:
  for j in A[1]:
    for k in A[2]:
      if sorted([i, j, k]) == [4, 5, 6]:
        ans += 1
print(ans/216)