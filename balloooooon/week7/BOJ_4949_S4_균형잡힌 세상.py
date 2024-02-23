import sys

input = sys.stdin.readline

while 1:
    a=input().rstrip()
    if a=='.':
        break
    stack=[]
    for i in a:
        if i=='[':
            stack.append(i)
        elif i=='(':
            stack.append(i)
        elif i==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(i)
                break
    print('yes') if not stack else print('no')