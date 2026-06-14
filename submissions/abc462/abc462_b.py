N = int(input())
lst = [[]for _ in range(N+1)]
for i in range(1, N+1):
    T = list(map(int, input().split()))
    for j in range(1,len(T)):
        lst[T[j]].append(i)
for p in lst[1:]:
    if len(p) >= 1:
        print(len(p), *p)
    else:
        print("0")