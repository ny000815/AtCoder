X = int(input())
X -= 1
S = 'HelloWorld'
for i in range(len(S)):
    if i == X:
        continue
    print(S[i], end='')
print("")