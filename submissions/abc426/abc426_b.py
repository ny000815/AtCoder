S = input()
S = sorted(S)
if S[0] == S[1]:
    print(S[-1])
else:
    print(S[0])