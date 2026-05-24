import math
T = int(input())
for i in range(T):
    S = input()
    cnt = [0] * 26
    for j in range(len(S)):
        cnt[ord(S[j]) - ord('a')] += 1
    if max(cnt) > math.ceil(len(S) / 2):
        print("No")
        continue

    print("Yes")
    prev = -1

    ans = []
    while True:
        val = 0
        idx = -1
        for n in range(26):
            if n == prev:
                continue
            if cnt[n] > val:
                idx = n
                val = cnt[n]
        if idx == -1:
            break
        ans.append(chr(idx + ord('a')))
        prev = idx
        cnt[idx] -= 1
    print("".join(ans))


