S = input()
alphabets = "abcdefghijklmnopqrstuvwxyz"
for c in alphabets:
    if c not in S:
        print(c)
        exit(0)