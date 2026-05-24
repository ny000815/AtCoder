import sys

input = sys.stdin.readline


def solve():
    s = input()[:-1]
    n = len(s)
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord("a")] += 1
    for v in cnt:
        if v > (n + 1) // 2:
            print("No")
            return
    ans = []
    prev = -1
    while True:
        idx = -1
        val = 0
        for i in range(26):
            if i == prev:
                continue
            if val < cnt[i]:
                val = cnt[i]
                idx = i
        if idx == -1:
            break
        ans.append(chr(ord("a") + idx))
        cnt[idx] -= 1
        prev = idx
    print("Yes")
    print("".join(ans))


for _ in range(int(input())):
    solve()
