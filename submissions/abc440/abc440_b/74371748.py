N = int(input())
T = list(map(int, input().split()))
TSorted = sorted(T)
for i in range(3):
  print(T.index(TSorted[i]) + 1, end = " ")