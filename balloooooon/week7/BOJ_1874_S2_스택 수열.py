'''
이 문제는 일단 설명부터가 불친절하다. 지문을 비문학으로 엮어놨다.
크게 세가지

1, 문제에서 요구한 리스트 num_list
2, 너의 스택 stack
3. num_list로 만들고 싶은 리스트 c
입력값으로 어떤 리스트를 문제에서 제시할 것이고, 네가 자연수를 스택 stack 에 1부터 넣을 수 있다. 넣을 수 있는 숫자는 1씩 증가한다, 제시된 리스트 num_list를 만들 수 있도록
스택에서 pop해서 c에 넣을 수 있다.

이를 구현하니 아래처럼 되었고, 시행착오를 겪어서 완성했다.
a, b, c는 편의상 써놓은 것이고 구현과정은 조금 다르다

'''

N = int(input())
answer = []
stack = []
num_list = []
for _ in range(N):
    temp = int(input())
    num_list.append(temp)

cur_num = 1
cur_index = 0 # 현재 num_list에서 stack의 값과 비교할 숫자의 인덱스
i=1 # 스택에 넣을 숫자
while cur_index < N:
    num = num_list[cur_index]
    if stack:
        if stack[-1] == num:
            stack.pop()
            cur_index += 1
            answer.append('-')
        else:
            stack.append(i)
            i += 1
            answer.append('+')
            if i > N+1:
                break
    else:
        stack.append(i)
        i += 1
        answer.append('+')

if cur_index != N:
    print('NO')
else:
    for str in answer:
        print(str)
