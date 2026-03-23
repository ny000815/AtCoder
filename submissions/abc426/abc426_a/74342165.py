X, Y = input().split()
OsVersions = {"Ocelot":0, "Serval":1, "Lynx":2}
print("Yes" if OsVersions[X] >= OsVersions[Y] else "No")