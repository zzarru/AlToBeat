# BOJ 15652 S3 N과 M (4)

"""
어제 푼 문제에서 가지치기 조건만 추가해주면 된다.
"""

import sys


def backtrack(current):
    if len(current) > 1 and current[-1] < current[-2]:
        return

    if len(current) == m:
        visited[current[-1]] = 0
        print(*current)
        return

    for j in range(1, n + 1):
        next_ = current + [j]
        if len(next_) == m:
            visited[j] = 1
        backtrack(next_)


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())

    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        backtrack([i])
