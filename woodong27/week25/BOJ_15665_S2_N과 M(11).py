# BOJ 15665 S2 N과 M (11)

import sys


def backtrack(current):
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
    numbers = list(set(map(int, enter().split())))
    numbers.sort()

    n = len(numbers)

    visited = [0] * n
    for i in range(n):
        backtrack([numbers[i]])
