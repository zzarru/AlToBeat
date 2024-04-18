group_num, quiz_num =map(int,input().split())
groups =[]
for i in range(group_num):
    group = []
    group.append(input())
    mem_num = int(input())
    for j in range(mem_num):
        group.append(input())
    groups.append(group)

for i in range(quiz_num):
    problem = input()
    quiz_type = int(input())
    if quiz_type:
        for group in groups:
            if problem in group:
                print(group[0])
                break
    else:
        for group in groups:
            if problem == group[0]:
                answer = group[1:]
                answer.sort()
                for member in answer:
                    print(member)
                break