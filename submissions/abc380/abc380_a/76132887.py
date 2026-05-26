N = input()
one, two, three = 0, 0, 0
for n in N:
    if n == '1':
        one += 1
    if n == '2':
        two += 1
    if n == '3':
        three += 1
print("Yes" if one == 1 and two == 2 and three == 3 else "No")