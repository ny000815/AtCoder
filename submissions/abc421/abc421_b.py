A = [0] * 10
A[0], A[1] = map(int, input().split())
for i in range(2, 10):
  A[i] = int(str(A[i - 2] +A[i - 1])[::-1])
print(A[9])