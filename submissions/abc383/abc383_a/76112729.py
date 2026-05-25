N = int(input())
time = [0]
w = 0
for i in range(1,N+1):
    T, V = map(int, input().split())
    time.append(T)
    w = max(0, w - (T - time[i-1]))
    w += V
print(w)