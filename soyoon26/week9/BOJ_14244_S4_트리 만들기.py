n,m=map(int,input().split())
print(0,1)
cnt=0
for i in range(2,n):
    print(1,i)
    cnt+=1
    if cnt==m-1:
        for j in range(i,n-1):
            print(j,j+1)

        break