N = int(input())
A = [0] + list(map(int, input().split()))
ans = [0] * (N + 1)


for i in range(N, 0, -1):
  if A[i] == i:
    ans[i] = i
  else:
    ans[i] = ans[A[i]]

for i in range(1, len(ans)):
  if i == 1:
    print(ans[i], end = "")
  else:
    print(" ", end = "")
    print(ans[i], end = "")
