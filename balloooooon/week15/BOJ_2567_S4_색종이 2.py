graph=[[0 for _ in range(102)] for _ in range(102)]
di=[-1,1,0,0]
dj=[0,0,-1,1]
for i in range(int(input())):
    a,b=map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            if not graph[i][j]:
                graph[i][j]=1

cnt=0

for i in range(102):
    for j in range(102):
        temp=0
        if graph[i][j]:
            for k in range(4):
                ni=i+di[k]
                nj=j+dj[k]
                if 0<=ni<102 and 0<=nj<102:
                    if graph[ni][nj]==0:
                        temp += 1

            if temp==1:
                cnt += 1
            elif temp==2:
                cnt += 2

print(cnt)


