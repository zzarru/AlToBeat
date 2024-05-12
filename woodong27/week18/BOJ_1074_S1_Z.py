# BOJ 1074 S1 Z

"""
분할정복 재귀 문제인데...
그냥 수학문제 같다.
당최 어떻게 할지 모르겠어서 그냥 찾아봤다.
"""


def divide(n, i, j):
    if not n:
        return 0
    current = 2 * (i % 2) + (j % 2)
    return 4 * divide(n - 1, i // 2, j // 2) + current


if __name__ == '__main__':
    N, R, C = map(int, input().split())
    answer = divide(N, R, C)
    print(answer)
