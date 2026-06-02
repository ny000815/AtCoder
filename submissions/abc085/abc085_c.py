N, Y = map(int, input().split())
resa, resb, resc = -1, -1, -1

for i in range(N + 1):
  for j in range(N - i + 1):
    k = N - i - j
    #if k < 0 or k > N:
      #continue
    if 10000*i + 5000*j + 1000*k == Y:
      resa, resb, resc = i, j, k
print(resa, resb, resc)