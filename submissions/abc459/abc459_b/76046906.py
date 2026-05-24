from collections import defaultdict
N = int(input())
tmp = input().split()
lst = []
for i in range(N):
    lst.append(tmp[i][0])


dict = defaultdict(int)
dict["a"] = 2
dict["b"] = 2
dict["c"] = 2

dict["d"] = 3
dict["e"] = 3
dict["f"] = 3

dict["g"] = 4
dict["h"] = 4
dict["i"] = 4

dict["j"] = 5
dict["k"] = 5
dict["l"] = 5

dict["m"] = 6
dict["n"] = 6
dict["o"] = 6

dict["p"] = 7
dict["q"] = 7
dict["r"] = 7
dict["s"] = 7

dict["t"] = 8
dict["u"] = 8
dict["v"] = 8

dict["w"] = 9
dict["x"] = 9
dict["y"] = 9
dict["z"] = 9

for l in lst:
    print(dict[l], end='')

print("")