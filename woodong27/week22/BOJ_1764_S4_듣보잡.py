# BOJ 1764 S4 듣보잡

"""
python의 set을 활용해서
듣도 못한 사람과 보도 못한 사람의 교집합을 구하면 된다.
"""

import sys


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())

    heard = set(enter().strip() for _ in range(n))
    seen = set(enter().strip() for _ in range(m))

    result = sorted(heard & seen)
    answer = '\n'.join(result)

    sys.stdout.write(f'{len(result)}\n')
    sys.stdout.write(f'{answer}\n')
