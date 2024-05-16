from collections import defaultdict

while 1:
    N = int(input())
    if not N:
        break
    else:
        dict = defaultdict(list)
        for i in range(N):
            name, length = input().split()
            dict[float(length)].append(name)
    print(*dict[max(dict)])

