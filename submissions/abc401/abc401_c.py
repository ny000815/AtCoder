N, K = map(int, input().split())
kBonacci = []
cumSum = [0]
kBonacci = [1 for i in range(N + 1)]
s = K
for i in range(K, N+1):
  kBonacci[i] = s
  s -= kBonacci[i-K]
  s += kBonacci[i]
  s %= 1000000000
print(kBonacci[N])