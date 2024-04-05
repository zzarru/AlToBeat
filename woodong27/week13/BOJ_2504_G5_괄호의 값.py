# BOJ 2504 G5 괄호의 값

"""
그냥 조건문 노가다 문제
너무 귀찮다.
"""

def calculate_brackets_value(brackets):
    stack = []

    for bracket in brackets:
        if bracket == '(' or bracket == '[':
            stack.append(bracket)
        elif bracket == ')':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    if temp == 0:
                        stack.append(2)
                    else:
                        stack.append(2 * temp)
                    break
                elif top == '[':
                    print(0)
                    return
                else:
                    temp += top
            else:
                print(0)
                return
        elif bracket == ']':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    if temp == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * temp)
                    break
                elif top == '(':
                    print(0)
                    return
                else:
                    temp += top
            else:
                print(0)
                return

    result = 0
    while stack:
        top = stack.pop()
        if top == '(' or top == '[':
            print(0)
            return
        result += top

    print(result)


brackets = input()
calculate_brackets_value(brackets)
