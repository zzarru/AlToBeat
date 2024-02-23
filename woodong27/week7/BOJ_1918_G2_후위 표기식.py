#BOJ 1918 G2 후위 표기식

"""
입력받은 수식을 하나씩 조회하며
여는 괄호랑 연산자는 stack에 넣고 숫자는 answer에 순서대로 추가해준다.
닫는 괄호를 만나면, 여는 괄호를 만날 때 까지 stack에 있는 수식들을
하나씩 뺴서 정답에 추가해준다.

괄호가 없는 식이면 연산자의 순위로 계산한다.
ops 라는 연산자의 순위를 정의한 딕셔너리를 만들어서
현재 stack의 top에 있는 연산자가 본인보다 순위가 같거나 큰 연산자라면
모두 빼서 순서대로 answer에 더해줘야한다.

싸피 1학기에 풀려다가 못 푼건데
지금은 생각보다 쉽게 풀어서 만족스럽다.
"""

formula = input()

ops = {'+': 0, '-': 0, '*': 1, '/': 1}

stack = []
answer = ''
for letter in formula:
    if letter.isalpha():
        answer += letter
    else:
        if letter == '(':
            stack.append(letter)
        elif letter == '+' or letter == '-' or letter == '*' or letter == '/':
            while stack and stack[-1] != '(' and ops[stack[-1]] >= ops[letter]:
                answer += stack.pop()
            stack.append(letter)
        elif letter == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()

while stack:
    answer += stack.pop()

print(answer)
