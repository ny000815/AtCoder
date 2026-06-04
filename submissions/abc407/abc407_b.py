X, Y = map(int, input().split())
falseCount = 0
for a in range(1,7):
    for b in range(1,7):
        if abs(a-b) < Y and a + b < X:
            falseCount += 1
print((36-falseCount)/36)