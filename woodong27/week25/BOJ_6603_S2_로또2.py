# BOJ 6603 S2 로또2

import sys


def backtrack(current, idx):
    if len(current) == 6:
        print(*current)

    for j in range(idx + 1, k):
        if not visited[j]:
            visited[j] = 1
            backtrack(current + [s[j]], j)
            visited[j] = 0


if __name__ == '__main__':
    enter = sys.stdin.readline

    while True:
        k, *s = map(int, enter().split())
        if not k:
            break

        visited = [0] * k
        for i in range(k):
            visited[i] = 1
            backtrack([s[i]], i)
            visited[i] = 0

        sys.stdout.write('\n')
