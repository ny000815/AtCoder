H = int(input())
def rec(H):
    if H == 1:
        return 1
    else:
        return rec(H // 2) * 2  + 1
print(rec(H))