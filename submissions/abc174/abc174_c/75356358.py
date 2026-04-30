K = int(input())
n = 0
isDivisable = False
for i in range(1, K + 1):
  n = (n * 10 + 7)%K 
  if n == 0:
    isDivisable = True
    break
  
print(i if isDivisable else -1)