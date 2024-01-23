# 백준 10825 S4 국영수

N = int(input())

students = []
for _ in range(N):
    temp = list(map(str, input().split()))
    students.append(temp)

# 1번 인덱스 기준 내림차순
# 2번 인덱스 기준 오름차순
# 3번 인덱스 기준 내림차순
# 0번 인덱스 기준 오름차순
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])
