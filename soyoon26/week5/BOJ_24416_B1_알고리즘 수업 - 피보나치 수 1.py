n=int(input())
f_lst=[1,1]+[0]*(n-2)
for i in range(2,n):
    f_lst[i]=f_lst[i-1]+f_lst[i-2]
print(f_lst[n-1],n-2)
