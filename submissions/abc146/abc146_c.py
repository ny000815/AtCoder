A, B, X = map(int, input().split())
right = 10 ** 9 + 1
left = 0

while right - left > 1:
    mid = (left + right) // 2
    if A * mid + B * len(str(mid)) > X:
        right = mid
    else:
        left = mid

print(left)