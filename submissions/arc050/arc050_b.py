R, B = map(int, input().split())
x, y = map(int, input().split())

def check(num):
    r = R - num
    l = B - num
    if r < 0 or l < 0:
        return False
    return r // (x-1) + l // (y-1) >= num

left = 0
right = 10 ** 18 +1
while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)