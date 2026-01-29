def factorial(n):
	res = 1
	for i in range(1, n+1):
		res *= i
	return res

P = int(input())
coin_count = 0
num = 1
while not factorial(num) >= P:
	num += 1
#print(num)
#print("")

temp = 0
for i in range(num, 0, -1):
  #print (f"i = {i}")
  f = factorial(i)
  while temp + f <= P:
    temp += f
    coin_count += 1
    #print(temp)
print(coin_count)