
card = [0 for _ in range(100)]
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        card.append(query[1])
    else:
        print(card.pop())

