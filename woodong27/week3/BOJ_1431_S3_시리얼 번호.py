# 백준 1431 S3 시리얼 번호

"""
1. 길이가 짧은 것이 먼저 온다.
2. 길이가 같다면, 모든 자리수에서 정수인 것들의 합을 비교해서 작은 것이 먼저 온다.
3. 1,2 로도 안되면 사전순으로 비교한다.(숫자가 알파벳보다 사전순으로 작다.)
"""


# 문자열에서 정수만 찾아서 합을 반환하는 메서드
def calculate_integers(letters):
    result = 0
    for letter in letters:
        if letter.isdigit():
            result += int(letter)

    return result


N = int(input())

guitars = []
for _ in range(N):
    guitars.append(input())

# 위의 조건 1, 2, 3에 맞게 정렬한다.
# 파이썬의 sort는 기본적으로 사전순 정렬을 제공하기 때문에 3번 조건은 그냥 그대로 넣으면 된다.
guitars.sort(key=lambda x: (len(x), calculate_integers(x), x))

for guitar in guitars:
    print(guitar)
