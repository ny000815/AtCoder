N, M = map(int, input().split())
options = [i for i in range(1, M + 1)]

for _ in range(N):
  L = input()
  X = list(map(int, input().split()))
  picked = -1
  for n in X:
    if picked == -1 and n in options:
      print(n)
      picked = n
      options.pop(options.index(n))
  if picked == -1:
    print(0)
