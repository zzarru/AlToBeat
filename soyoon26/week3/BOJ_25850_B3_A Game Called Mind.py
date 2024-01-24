N = int(input())
num=[]
card=[]
people=['A','B','C','D','E','F']
for i in range(N):
    card=list(map(int,input().split()))
    for j in range(1,card[0]+1):
        num.append({people[i]:card[j]})
def quick(lst):
    if len(lst) <= 1:
        return lst
    pv=list(lst[0].values())[0]
    tail = lst[1:]
    left=[x for x in tail if list(x.values())[0] <= pv]
    right=[x for x in tail if list(x.values())[0] > pv]
    return quick(left)+[lst[0]]+quick(right)
answer = ''.join([list(i.keys())[0] for i in quick(num)])
print(answer)

#퀵정렬