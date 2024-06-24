# BOJ 15656 S3 N과 M (7)

import sys


def backtrack(current):
    if len(current) == m:
        visited[numbers.index(current[-1])] = 0
        print(*current)
        return

    for j in range(n):
        if not visited[j]:
            next_ = current + [numbers[j]]
            if len(next_) == m:
                visited[j] = 1
            backtrack(current + [numbers[j]])


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())
    numbers = list(map(int, enter().split()))
    numbers.sort()

    visited = [0] * n
    for i in range(n):
        backtrack([numbers[i]])
