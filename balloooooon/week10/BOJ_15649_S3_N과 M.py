n,m=map(int,input().split())
visited=[0]*(n+1)
stack=[]
def per(a,m):
    if a==m:
        print(*stack)
    else:
        for i in range(1,n+1):
            if not visited[i]:
                visited[i]=True
                stack.append(i)
                per(a+1,m)
                visited[i]=False
                stack.pop()
per(0,m)