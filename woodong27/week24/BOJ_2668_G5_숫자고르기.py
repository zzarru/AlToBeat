# BOJ 2668 G5 숫자고르기

import sys


def dfs(start):
    visited = set()
    stack = []
    current = start

    while current not in visited:
        visited.add(current)
        stack.append(current)
        current = number[current]

    if current in stack:
        start = stack.index(current)
        result.update(stack[start:])


if __name__ == '__main__':
    sys.setrecursionlimit(100 ** 2)
    enter = sys.stdin.readline
    n = int(enter())
    number = [0] + [int(enter()) for _ in range(n)]

    result = set()
    for i in range(1, n + 1):
        if i not in result:
            dfs(i)

    sys.stdout.write(f'{len(result)}\n')
    print(*sorted(result), sep='\n')
