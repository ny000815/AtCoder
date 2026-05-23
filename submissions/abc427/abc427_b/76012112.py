N = int(input())
ls = [1, 1]

def calDigitSum(n):
    num = n
    ans = 0
    while num > 0:
        ans += num % 10
        num //= 10
    return ans

ans = 0
for i in range(2, N+1):
    num = 0
    for j in range(i):
        num += calDigitSum(ls[j])
    ls.append(num)
print(ls[N])