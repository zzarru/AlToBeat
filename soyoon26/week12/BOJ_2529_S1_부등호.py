import sys
N = int(sys.stdin.readline().rstrip())
lst= list(sys.stdin.readline().split())
num=[1,2,3,4,5,6,7,8,9,0]
answer=[]
answer_candi=[]
def comp(answer,lst):
    global answer_candi
    cnt=0
    for i in range(len(lst)):
        if lst[i] == '<':
            if answer[i] < answer[i+1]:
                cnt+=1
            else:
                break
        elif lst[i] == '>':
            if answer[i] > answer[i+1]:
                cnt+=1
            else:
                break
    if cnt == len(lst):
        answer_candi.append(answer[:])
        return answer_candi

def back():
    global answer_candi
    if len(answer) == len(lst)+1:
        comp(answer,lst)
        return
    for i in num:
        if i not in answer:
            answer.append(i)
            back()
            answer.pop()
back()
print(*max(answer_candi),sep='')
print(*min(answer_candi),sep='')


