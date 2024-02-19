N = int(input())
for i in range(N):
    str_list = list(input())
    stack = []
    for str in str_list:
        if str == '(': # 여는 꺽쇠라면 무조건 스택에 담는다
            stack.append(str)
        else: # 만일 닫는 꺽쇠라면 두가지 경우, 스택이 있을때, 없을때
            if stack: # 있을때는 상쇄될 가능성이 있다.
                if stack[-1] == '(':
                    stack.pop()
                else: #만일 스택에서 꺼낸게 여는꺽쇠가 아니면 바로 탈출
                    break
            else: # 만일 닫는 꺽쇠가 여는 꺽쇠도 없는데 스택에 들어오면 바로 컷
                stack.append(str)
                break
    if stack:
        print('NO')
    else:
        print('YES')