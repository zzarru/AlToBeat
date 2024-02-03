# 2908_상수
'''
- 두 수 A, B가 주어질 때 거꾸로 읽었을 때 큰 수를 출력
- 예 : 751 234 -> 157 432 -> 답은 432로 출력
- 세 자리 수이며, 0이 포함되지 않음
'''

A, B = map(str, input().split())

new_A = ''
new_B = ''

for i in range(2, -1, -1):
    new_A += A[i]
    new_B += B[i]

int(new_A)
int(new_B)

if new_A > new_B:
    print(new_A)
else:
    print(new_B)
