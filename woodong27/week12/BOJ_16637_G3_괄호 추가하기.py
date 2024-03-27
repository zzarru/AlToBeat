# BOJ 16637 G3 괄호 추가하기

"""
연산자는 모두 1, 3, 5와 같은 홀수번째 index에 위치
숫자는 모두 짝수번째 index
현재 연산자에서 괄호를 쓰면, 다음 연산자에서는 괄호를 쓸 수 없고 다다음 연산자부터 가능
"""

n = int(input())
formula = input()


def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    if op == '*':
        return num1 * num2
    if op == '-':
        return num1 - num2


def dfs(idx, value):
    global answer
    if idx == n-1:
        answer = max(answer, value)
        return

    # 괄호 x
    # 현재 연산자 계산
    if idx + 2 < n:  # 다다음 연산자가 없음
        dfs(idx + 2, calculate(value, int(formula[idx + 2]), formula[idx + 1]))

    # 괄호를 추가할 수 있을 때
    # 다음번 연산자 계산을 괄호로 묶어서 먼저 계산
    if idx + 4 < n:  # 다다음 연산자가 있을 경우
        dfs(idx + 4, calculate(value, calculate(int(formula[idx + 2]), int(formula[idx + 4]), formula[idx + 3]), formula[idx + 1]))


answer = float('-inf')  # 결과의 범위가 2^-31 ~ 2^31이라 최악의 경우르 매우 작은 수를 사용
dfs(0, int(formula[0]))
print(answer)
