import math
T = int(input())

for i in range(T):
    X1, Y1, R1, X2, Y2, R2 = map(int, input().split())
    distX = abs(X1 - X2)**2
    distY = abs(Y1 - Y2)**2
    if R2 > R1:
        R1, R2 = R2, R1

    if (R1 + R2) ** 2 < distX + distY or distX + distY < (R1 - R2) ** 2:
        print("No")
    else:
        print("Yes")
