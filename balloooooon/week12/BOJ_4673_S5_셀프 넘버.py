def d(n):
    a=[]
    for i in str(n):
        a.append(int(i))
    return sum(a)+n
mom=[i for i in range(1,10001)]        
cost=[]
answer=[]
for i in range(1,10001):
    cost.append(d(i))
for i in mom:
    if i not in cost:
        answer.append(i)
for i in answer:
    print(i)