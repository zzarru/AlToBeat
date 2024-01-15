# 11021_A+B - 7
# week2 주제인 입출력과 관련된 문제
'''
- 두 정수 A+B를 입력받은 다음, A+B 출력
- 케이스마다 "Case #x:"를 출력, 케이스 번호는 1부터 시작
'''

T = int(input())

for t in range(1, T + 1):
    i, j = map(int, input().split())
    print(f"Case #{t}:", i + j)
