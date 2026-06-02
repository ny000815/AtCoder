X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())
armed = set()
armerWeight = 0
for _ in range(Q):
  P = int(input())
  P -= 1
  if P not in armed:
    armed.add(P)
    armerWeight += W[P]
    print(X + armerWeight)
  else:
    armed.remove(P)
    armerWeight -= W[P]
    print(X + armerWeight)