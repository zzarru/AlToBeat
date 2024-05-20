import sys
input = sys.stdin.readline

t = int(input())
S = []
for _ in range(t):
    inputs = list(map(str, input().split()))
    method = inputs[0]

    if method == 'all':
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    elif method == 'empty':
        S = []

    else:
        x = int(inputs[1])
        if x in S:
            if method in ['remove', 'toggle']:
                S.remove(x)
            elif method == 'check':
                print(1)

        else:
            if method in ['add', 'toggle']:
                S.append(x)
            elif method == 'check':
                print(0)