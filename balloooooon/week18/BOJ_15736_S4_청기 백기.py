start = 1
N = int(input())
if N == 1:
    print(1)
else:
    while 1:
        if start * start >= N:
            print(start-1)
            break
        start += 1

