'''
시행착오를 많이 겪어서 힘들었다..
'''

N, goal = map(int,input().split())
num_list = list(map(int,input().split()))
left = 0
right = 0
answer = 0
temp = num_list[left]
while 1:
    if temp == goal:
        answer += 1


    if temp >= goal:
        if left < N:
            pass
        else:
            break
        temp -= num_list[left]
        left += 1

    else:
        right += 1
        if right < N:
            temp += num_list[right]
        else:
            break
print(answer)