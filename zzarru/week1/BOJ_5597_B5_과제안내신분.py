students = list(range(1, 31))

for i in range(28):
    good_student = int(input())
    students.remove(good_student)

for bad_student in students:
    print(bad_student)