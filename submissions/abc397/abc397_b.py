S = input()
oddevenCnt = 0
for i in range(len(S)):
    if (i + oddevenCnt) % 2 == 0 and S[i] == 'o':
        oddevenCnt += 1
    if (i + oddevenCnt) % 2 == 1 and S[i] == 'i':
        oddevenCnt += 1
print(oddevenCnt + 1 if (oddevenCnt + len(S))%2 != 0 else oddevenCnt)