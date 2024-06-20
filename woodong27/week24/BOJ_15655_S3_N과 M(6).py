# BOJ 15655 S3 N과 M (6)

import sys


def backtrack(current):
    if len(current) > 1 and current[-1] < current[-2]:
        return

    if len(current) == m:
        print(*current)
        return

    for j in range(n):
        if not visited[j]:
            visited[j] = 1
            backtrack(current + [numbers[j]])
            visited[j] = 0


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())
    numbers = list(map(int, enter().split()))
    numbers.sort()

    visited = [0] * n
    for i in range(n):
        visited[i] = 1
        backtrack([numbers[i]])
        visited[i] = 0
