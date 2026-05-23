from collections import defaultdict
N, K = map(int, input().split())
S = input()
lst = defaultdict(int)
for i in range(N-K+1):
    lst[S[i:i+K]] += 1
maxNum = max(lst.values())
print(maxNum)
ans = []
for key, value in lst.items():
    if value == maxNum:
        ans.append(key)
print(*sorted(ans))
