'''
이 문제는 프린터기에 들어가는 용지의 우선순위가 가장 높은것부터 차례대로 뽑고 우선순위가 낮은건은 큐의 맨뒤로 옮기는 형식으로 진행한다
문제에서 요구하는 것은 제시한 용지가 언제 뽑힐지인데 용지에 이름이 적혀있는것이 아니기때문에
이름을 어떻게 붙여줘야 하는지가 고민이었다.
그래서 문제에서 제시한 용지에 이름을 붙여주고자 float type으로 만들어 버렸으며
적절한 조건문을 통해 답을 도출할 수 있도록 코드를 짰다.
'''

for _ in range(int(input())):
    N, order = map(int,input().split())
    queue = list(map(int,input().split()))
    queue[order] += 0.1
    answer = 0
    while 1:
        priority = int(max(queue))
        temp = queue.pop(0)
        if type(temp) == int and temp == priority:
            answer += 1
        elif type(temp) == float and int(temp) == priority:
            answer += 1
            print(answer)
            break
        else:
            queue.append(temp)