S = input()
T = input()
check = []
for i in range(1, len(S)):
    if S[i].isupper():
        check.append(S[i-1])
for l in check:
    if l not in T:
        print("No")
        exit()
print("Yes")