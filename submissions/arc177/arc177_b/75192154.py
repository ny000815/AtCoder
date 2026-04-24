N = int(input())
S = input()
solution = ""
for i in range(N-1, -1, -1):
  if S[i] == '1':
    solution += ('A'*(i+1))
    solution += ('B'*i)
print(len(solution))
print(solution)