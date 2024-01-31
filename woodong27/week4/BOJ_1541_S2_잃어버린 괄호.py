# BOJ 1541 S2 잃어버린 괄호

"""
수식을 계산했을 때 가장 작은 결과를 반환하도록 해야한다.
-를 기준으로 식들을 나눠서, 가장 마지막에 - 연산을 진행하면 된다.
"""

formula = input()

# - 으로 split을 하면, - 부호를 기준으로 식들이 나누어진다.
bracketed_with_minus = formula.split('-')

# -를 기준으로 나누어진 식 들에서 + 연산을 해서 리스트에 넣는다.
result = []
for numbers_with_plus in bracketed_with_minus:
    temp = 0
    numbers = numbers_with_plus.split('+')
    for number in numbers:
        temp += int(number)

    result.append(temp)

# 첫번째 원소를 뺴고는 전부 -해준다.
answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]

print(answer)
