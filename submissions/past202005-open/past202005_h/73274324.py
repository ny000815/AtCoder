N, L = map(int, input().split())
x = list(map(int, input().split()))
T = list(map(int, input().split()))

hurdles = [False] * (L + 1)
for v in x:
  hurdles[v] = True

times = [10**10] * (L + 1)
times[0] = 0


for i in range(1, L + 1):
  if i >= 1:
    times[i] = min(times[i], times[i - 1] + T[0])
  if i >= 2:
    times[i] = min(times[i], times[i - 2] + T[0] + T[1])
  if i >= 4:
    times[i] = min(times[i], times[i - 4] + T[0] + 3 * T[1])
  if hurdles[i]:
    times[i] += T[2]

for i in [L - 1, L - 2, L - 3]:
  if i >= 0:
    times[L] = min(times[L], times[i] + T[0] // 2 + T[1] //2 + T[1] * ((L - i) - 1))

print(times[L])