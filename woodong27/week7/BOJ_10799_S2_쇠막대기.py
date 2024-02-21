# BOJ 10799 S2 쇠막대기

"""
1. ()는 레이저로 미리 replace하고 시작한다
2. (일 경우에는 쇠막대기의 시작점이므로 stack에 넣는다.
2. laser를 만날 경우에는 현재 stack에 들어있는 막댁기의 수 만큼 잘리게 되므로 더해준다.
3. )를 만나면 쇠막대기 하나가 끝나는 것이므로 stack에서 제거하고 하나가 추가되는 만큼 1을 더해준다.
"""

brackets = input()
brackets = brackets.replace('()', 'l')

stack = []
answer = 0
for bracket in brackets:
    if bracket == 'l':
        answer += len(stack)
    elif bracket == '(':
        stack.append(bracket)
    else:
        stack.pop()
        answer += 1

print(answer)
