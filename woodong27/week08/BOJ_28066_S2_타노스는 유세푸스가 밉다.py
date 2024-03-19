# BOJ 28066 S2 타노스는 유세푸스가 밉다

import sys
from collections import deque

"""
처음에는 굳이 큐로 풀 필요가 없을 것 같아서
first = squirrels[0]
squirrels = squirrels[k:]
squirrels.append(first)
이렇게 풀었는데, 계속해서 시간초과가 발생했다.

반면 큐를 사용해서 popleft()와 append()로 푸니까 시간초과가 발생하지 않았다.
-> 리스트 슬라이싱 보다 큐의 pop이 더 빠른 것 같다.
"""

n, k = map(int, sys.stdin.readline().strip().split())

squirrels = deque([i for i in range(1, n + 1)])

while True:
    if len(squirrels) < k:
        print(squirrels[0])
        break
    else:
        first = squirrels.popleft()
        temp = []
        while True:
            if len(temp) >= k - 1:
                break
            temp.append(squirrels.popleft())
        squirrels.append(first)
