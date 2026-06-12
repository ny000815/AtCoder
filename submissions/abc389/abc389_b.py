X = int(input())
num = 1
for i in range(1, X+2):
    num *= i
    if num >= X:
        print(i)
        exit()