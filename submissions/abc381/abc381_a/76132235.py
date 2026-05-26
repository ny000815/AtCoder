N = int(input())
S = input()
mid = (len(S) + 1) // 2 - 1
isValid = True
for i in range(N):
    if i < mid and S[i] != '1':
        isValid = False
        break
    elif i == mid and S[i] != '/':
        isValid = False
        break
    elif i > mid and S[i] != '2':
        isValid = False
        break
print("Yes" if isValid and N % 2 != 0 else "No")

