T = int(input())
for _ in range(T):
    PS = input()
    ans = 'YES'
    opened = []
    for i in PS:
        if len(opened) == 0: # 여는 괄호가 없고 닫는 괄호가 먼저 나오면
            if i == ')':
                ans = 'NO'
                break
            else:
                opened.append(i)

        else: # 여는 괄호가 있고 닫는 괄호가 나오면
            if i == ')':
                opened.pop()
            else:
                opened.append(i)

    if len(opened) != 0:
        ans = 'NO'

    print(ans)