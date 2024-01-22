# 백준 2108 S3 통계학

import sys

'''
입력받는 정수의 갯수가 최대 50만개
input()과 sum()을 사용했을 떄 시간초과가 발생했다.
-> 시간을 줄이기 위해 숫자를 입력받을 때 마다 바로 더해서 sum값을 미리 구하고
input()대신 sys.stdin.readline()을 사용했다.
'''

N = int(sys.stdin.readline())

# 입력받는 숫자들을 저장할 리스트
numbers = []
# 입력받는 숫자들의 갯수를 저장할 딕셔너리
numbers_dict = {}
# 합을 저장할 변수
total_sum = 0
for _ in range(N):
    number = int(sys.stdin.readline())
    total_sum += number
    numbers.append(number)
    if number in numbers_dict:
        numbers_dict[number] += 1
    else:
        numbers_dict[number] = 1

# 배열을 오름차순 정렬
numbers.sort()

# 산술 평균
print(round(total_sum / N))

# 중앙값
print(numbers[N//2])

# 최빈값
# 최빈값들을 저장할 임시 리스트
temp = []
max_value = max(numbers_dict.values())
# 딕셔너리를 조회하며, 최빈값들을 temp에 저장한다.
for key, value in numbers_dict.items():
    if value == max_value:
        temp.append(key)

# temp의 길이가 1(==최빈값이 한개)
if len(temp) == 1:
    print(temp[0])
# temp의 길이가 2 이상(==최빈값이 두개 이상)
else:
    temp.sort()
    print(temp[1])

# 입력받는 숫자들의 범위
print(numbers[-1] - numbers[0])
