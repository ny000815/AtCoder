A, B, W = map(int, input().split())
W *= 1000
ans = []
for n in range(1, W//A+1):
    if n*A <= W <= n*B:
        ans.append(n)
ans.sort()
if ans:
    print(ans[0], end = " ")
    print(ans[-1])
else:
    print("UNSATISFIABLE")