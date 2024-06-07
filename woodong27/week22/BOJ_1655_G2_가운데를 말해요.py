# BOJ 1655 G2 가운데를 말해요

"""
최대힙과 최소힙 두가지를 만들고
최대힙의 루트에 항상 가운데값이 위치하도록 조정한다.
"""

import sys
from heapq import heappush, heappop


if __name__ == '__main__':
    enter = sys.stdin.readline
    n = int(enter())

    max_heap = []  # 최대 힙
    min_heap = []  # 최소 힙

    for _ in range(n):
        num = int(enter())

        if len(max_heap) == len(min_heap):
            heappush(max_heap, -num)
        else:
            heappush(min_heap, num)

        if min_heap and -max_heap[0] > min_heap[0]:
            max_val = -heappop(max_heap)
            min_val = heappop(min_heap)
            heappush(max_heap, -min_val)
            heappush(min_heap, max_val)

        sys.stdout.write(f'{-max_heap[0]}\n')
