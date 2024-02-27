import sys
input = sys.stdin.readline

T = int(input())
queue = []
for _ in range(T):
    command = input().split()
    order = command[0]

    if order == 'push':
        queue.append(command[1])
    elif order == 'pop':
        if queue:
            print(queue[0])
            queue.pop(0)
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)