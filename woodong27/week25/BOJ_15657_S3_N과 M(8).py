# BOJ 15657 S3 N과 M (8)

import sys


def backtrack(current):
    if len(current) > 1 and current[-1] < current[-2]:
        return

    if len(current) == m:
        visited[numbers.index(current[-1])] = 1
        print(*current)
        return

    for j in range(n):
        if not visited[j]:
            backtrack(current + [numbers[j]])
            visited[j] = 0


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())
    numbers = list(map(int, enter().split()))
    numbers.sort()

    visited = [0] * n
    for i in range(n):
        backtrack([numbers[i]])
