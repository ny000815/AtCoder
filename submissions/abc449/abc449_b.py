H, W, Q = map(int, input().split())
for i in range(Q):
  qtype, num = map(int, input().split())
  if qtype == 1:
    print(num*W)
    H -= num
  else:
    print(num*H)
    W -= num