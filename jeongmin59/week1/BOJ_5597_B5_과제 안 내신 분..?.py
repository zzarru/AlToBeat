# 5597_과제 안 내신 분..?
'''
- 1번부터 30번까지 출석 번호가 붙어져 있음
- 과제 제출 안 한 2명의 출석 번호 구하기
- 출력 시 1번째 줄에는 제출하지 않은 학생 번호 중 가장 작은 것, 그 다음 번호 출력
- 출석 번호에 중복 없음
'''

student = [i for i in range(1, 31)]

for _ in range(28):
    x = int(input())
    student.remove(x)
    student.sort()

for s in student:
    print(s)

'''
- 잊고 있었던 거
remove()
sort()
'''
