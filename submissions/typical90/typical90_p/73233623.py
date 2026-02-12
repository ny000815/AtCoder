N = int(input())
ABC = list(map(int, input().split()))

coinNum = 2 ** 60
for i in range(10000):
  for j in range(10000):
    k = N - ABC[0] * i - ABC[1]*j
    if k >= 0 and k % ABC[2] == 0:
      k_coins = k // ABC[2]
      coinNum = min(i + j + k_coins, coinNum)
    
print(coinNum)