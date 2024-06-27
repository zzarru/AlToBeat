a=int(input())
list1=list(map(int,input().split()))

sec=[]
for i in list1:
    sec.append((i/max(list1)*100))
print(sum(sec)/a)