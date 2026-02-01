N = int(input())
A = list(map(int, input().split()))

cnt = sum(n < 0 for n in A)
minnum = min(map(abs, A))
abssum = sum(map(abs, A))

print(abssum if cnt % 2 == 0 else abssum - minnum * 2)