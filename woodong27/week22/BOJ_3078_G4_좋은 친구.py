# BOJ 3078 G4 좋은 친구

"""
처음엔 q를 사용했었는데
defaultdict을 사용해서 간단하게 풀었다.
"""

import sys
from collections import defaultdict


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, k = map(int, enter().split())
    friends = [len(enter().strip()) for i in range(n)]

    answer = 0
    count = defaultdict(int)

    for i in range(n):
        if i > k:
            count[friends[i - k - 1]] -= 1

        answer += count[friends[i]]
        count[friends[i]] += 1

    sys.stdout.write(f'{answer}\n')
