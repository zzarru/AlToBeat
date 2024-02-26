stock=[]
for i in range(int(input())):
    line=list(map(int,input().split()))
    stock.append(line)
stock.sort(key=lambda x:x[0])
height=[]
a=[]
cnt=0
for i in range(len(stock)):
    a.append(stock[i][0])
for i in range(len(stock)):
    height.append(stock[i][1])
square=[0]*(stock[-1][0]+1)
for i,j in stock:
    square[i]=j
for i in range(len(square)):

    if 0<i<len(square)-1:
        left=max(square[:i])
        right=max(square[i+1:])
        middle=min(left,right)
        if middle>square[i]:
            square[i]=middle


print(sum(square))