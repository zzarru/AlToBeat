T=int(input())
for t in range(T):
    x=int(input())
    f_lst=[1,1]+[0]*(x-1)
    for i in range(2,x+1):
        f_lst[i] = f_lst[i-2]+f_lst[i-1]
    print(f_lst[x])