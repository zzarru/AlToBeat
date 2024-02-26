'''
200만개까지의 악의적인 테스트케이스가 도사리고 있으므로,
빠른 입력을 받음으로 시간을 줄여주었다.
'''
 
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())

queue = deque()


for _ in range(N):
    order = input().rstrip()

    if len(order) >= 6:
        num = int(order[5:])
        queue.append(num)
    else:
        if order == 'front':
            print(queue[0]) if queue else print(-1)
        elif order == 'pop':
            print(queue.popleft()) if queue else print(-1)
        elif order == 'size':
            print(len(queue))
        elif order == 'empty':
            print(0) if queue else print(1)
        elif order == 'back':
            print(queue[-1]) if queue else print(-1)

