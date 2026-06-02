from traceback import print_tb

N, c1, c2 = input().split()
S = input()
ans = []
for l in S:
    if l == c1:
        ans.append(c1)
    else:
        ans.append(c2)
print("".join(ans))