# BOJ 31804 G4 Chance!

"""
chance를 썼을 때와 쓰지 않았을 때로 구분해서
visited를 체크하고 bfs 탐색을 진행했다.
"""

import sys
from collections import deque


def bfs(start):
    q = deque([[start, 0]])
    visited = [[0, 0] for _ in range(b + 1)]
    visited[start][0] = 1

    while q:
        current, is_chance_used = q.popleft()
        if current == b:
            return visited[current]

        next1, next2 = current + 1, current * 2
        if not is_chance_used:
            next3 = current * 10
            if next3 <= b and not visited[next3][0]:
                visited[next3][1] = visited[current][0] + 1
                q.append([next3, 1])

        if next1 <= b and not visited[next1][is_chance_used]:
            visited[next1][is_chance_used] = visited[current][is_chance_used] + 1
            q.append([next1, is_chance_used])

        if next2 <= b and not visited[next2][is_chance_used]:
            visited[next2][is_chance_used] = visited[current][is_chance_used] + 1
            q.append([next2, is_chance_used])


if __name__ == '__main__':
    enter = sys.stdin.readline
    a, b = map(int, enter().split())

    result = bfs(a)
    answer = max([value for value in result if value]) - 1
    sys.stdout.write(f'{answer}\n')
