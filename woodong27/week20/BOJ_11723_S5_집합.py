# BOJ 11723 S5 집합

import sys

"""
분류는 비트마스킹인데
이름부터가 집합이라 그냥 set으로 풀었다.
"""


def bit_masking(op, num):
    """
    비트마스킹 풀이
    :param op: 연산자
    :param num: 숫자
    :return:
    """
    global s
    if op == 'add':
        s = s | (0b1 << num)
    elif op == 'remove':
        s = s & ~(0b1 << num)
    elif op == 'check':
        if s & (0b1 << num):
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        s = s ^ (0b1 << num)


def operation(op, num):
    """
    집합을 사용한 풀이
    :param op:
    :param num: 
    :return:
    """
    global s
    if op == 'add':
        s.add(num)
    elif op == 'remove':
        s.discard(num)
    elif op == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if num in s:
            s.discard(num)
        else:
            s.add(num)


if __name__ == '__main__':
    enter = sys.stdin.readline
    m = int(enter())

    # s = set()
    s = 0b0
    for _ in range(m):
        temp = enter().strip().split()
        if len(temp) == 1:
            if temp[0] == 'all':
                # s = set([i for i in range(1, 21)])
                s = 0b111111111111111111111
            else:
                # s = set()
                s = 0b0
        else:
            order, number = temp[0], int(temp[1])
            # operation(order, number)
            bit_masking(order, number)