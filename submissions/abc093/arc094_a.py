num = list(map(int, input().split()))

num.sort()
diff2 = num[2] - num[1]
num[0] += diff2
diff1 = max(num[2] - num[0], 0)
if diff1 % 2 == 0:
    print(diff1 // 2 +diff2)
else:
    print(diff1 // 2 + 2 + diff2)