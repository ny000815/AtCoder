N, Q = map(int, input().split())
S = input()
cumSum = [0] * N
for i in range(1, N):
  cumSum[i] = cumSum[i - 1]
  if S[i - 1] == 'A' and S[i] == 'C':#using cumSUm by mistake
    cumSum[i] += 1#forgetting [i]
for _ in range(Q):
  l, r = map(int, input().split())#forgetting.split()
  l -= 1
  r -= 1
  print(cumSum[r] - cumSum[l])  