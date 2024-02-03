# BOJ 12891 S2 DNA  비밀번호

"""
슬리이딩 윈도우를 사용하는 문제
같은 사이즈의 배열이 한칸씩 오른쪽(or 왼쪽)으로 이동하기 때문에
사이즈를 유지하면서 한 칸씩 이동해서 값을 비교해주면 된다.
"""

import sys

enter = sys.stdin.readline

s, p = map(int, enter().strip().split())
DNAs = enter().strip()
a, c, g, t = map(int, enter().strip().split())

agct = {'A': 0, 'G': 0, 'C': 0, 'T': 0}

left, right = 0, p - 1
temp = DNAs[left:right + 1]
for DNA in temp:
    agct[DNA] += 1

answer = 0
while True:
    if agct['A'] >= a and agct['G'] >= g and agct['C'] >= c and agct['T'] >= t:
        answer += 1

    if right + 1 >= len(DNAs):
        break

    agct[DNAs[left]] -= 1
    left += 1
    right += 1
    agct[DNAs[right]] += 1

print(answer)
