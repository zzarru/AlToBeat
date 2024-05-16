# BOJ 1865 G3 웜폴

"""
벨만포드 알고리즘을 구현하면 되는 문제
시간초과가 발생해서 pypy3랑 sys.stdin.readline도 썼다.
그래도 시간초과가 발생해서 distance 리스트에 변경이 생기지 않으면 조기종료 시켜줬다.
"""

import sys


def bellman_ford(start):
    distance = [float('inf')] * n
    distance[start] = 0

    for _ in range(n-1):
        is_updated = False
        for i in range(n):
            for node, weight in points[i]:
                if distance[i] + weight < distance[node]:
                    distance[node] = distance[i] + weight
                    is_updated = True

        if not is_updated:
            break

    for i in range(n):
        for node, weight in points[i]:
            if distance[i] + weight < distance[node]:
                return True

    return False


if __name__ == '__main__':
    enter = sys.stdin.readline
    tc = int(enter())
    for _ in range(tc):
        n, m, w = map(int, enter().strip().split())
        points = [[] for _ in range(n)]
        for __ in range(m):
            s, e, t = map(int, enter().strip().split())
            points[s-1].append([e-1, t])
            points[e-1].append([s-1, t])

        for ___ in range(w):
            s, e, t = map(int, enter().strip().split())
            points[s-1].append([e-1, -t])

        answer = 'NO'
        for i in range(n):
            if bellman_ford(i):
                answer = 'YES'
                break

        print(answer)
