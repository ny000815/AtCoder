X = list(input())
X.sort()
ans = ""
zerocnt = 0
for i in range(0, len(X)):
    if X[i] == '0':
        zerocnt += 1
    else:
        ans += X[i]
print(ans[0] + "0" * zerocnt + ans[1:])
