T = input()
U = input()
for i in range(len(T)-len(U)+1):
    isValid = True
    for j in range(len(U)):
        if T[j+i] == "?":
            continue
        if U[j] != T[j+i]:
            isValid = False
            break
    if isValid:
        print("Yes")
        exit()
print("No")