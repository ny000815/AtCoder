N, M = map(int, input().split())

foodList = [0] * (M + 1)
for _ in range(N):
  A = list(map(int, input().split()))
  for i in range(A[0]):
    foodList[A[i + 1]] += 1

print(foodList.count(N))