from collections import defaultdict
arrays = defaultdict(int)
N = int(input())
for i in range(N):
  arrays[i+1] = list(map(int, input().split()))
X, Y = map(int, input().split())
print(arrays[X][Y])

