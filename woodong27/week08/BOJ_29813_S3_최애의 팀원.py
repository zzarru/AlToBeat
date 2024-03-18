# BOJ 29813 S3 최애의 팀원

"""
나의 짝은 내 학번 - 1 만큼 패스하고 나서 만나는 학생
큐에서 학생을 한명 빼고, 내 학번 - 1 만큼 append(popleft())
를 만복한 뒤에 한 번더 popleft()했을 때 만나는 학생이
나의 짝이다
"""

from collections import deque

n = int(input())
students = deque([])
for i in range(n):
    students.append(list(input().split()))

while len(students) > 1:
    name, number = students.popleft()
    count = 0
    while count < int(number) - 1:
        students.append(students.popleft())
        count += 1
    students.popleft()

print(students[0][0])
