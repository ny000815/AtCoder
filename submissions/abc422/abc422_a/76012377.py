S = input()
if S[2] == '8':
    print(int(S[0]) + 1, "-", "1", sep = "")
else:
    print(S[0], "-", int(S[2]) + 1, sep = "")