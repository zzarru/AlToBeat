import sys
input = sys.stdin.readline

N = int(input())

exam = []
for _ in range(N):
    point = tuple(map(str, input().split()))
    exam.append(point)

result = sorted(exam, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in result:
    print(student[0])