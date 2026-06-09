N, M = map(int, input().split())
A = list(map(int, input().split()))

def check(lst):
    checked = [0 for _ in range(M)]
    for a in lst:
        checked[a-1] = 1
    return 0 in checked

ans = 0
for i in range(N):
    if check(A):
        print(ans)
        exit(0)
    A = A[:-1]
    ans += 1
print(N)