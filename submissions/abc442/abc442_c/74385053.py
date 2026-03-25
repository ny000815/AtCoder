N, M = map(int, input().split())
nums = {}
for i in range(M):
  A, B = map(int, input().split())
  nums.setdefault(A, set()).add(B)
  nums.setdefault(B, set()).add(A)

for i in range(1, N+1):
  ir = N - len(nums.get(i, set())) - 1
  print(ir * (ir -1) * (ir - 2) // 6, end = " ")