# BOJ 17952 S3 과제는 끝나지 않아!

"""
stack은 후입 선출이기 때문에
과제가 들어올 때 마다 stack에 넣어주고
이번 시간에 과제가 하나 끝난 다면 점수를 더해주면 된다.

input으로 시간초과 떠서 stdin 사용
"""

import sys

enter = sys.stdin.readline

n = int(enter())

works = []
answer = 0
for _ in range(n):
    entry = list(map(int, enter().strip().split()))
    if entry[0]:
        works.append((entry[1], entry[2]))

    if works:
        score, time = works.pop()
        time -= 1
        if not time:
            answer += score
        else:
            works.append((score, time))

print(answer)
