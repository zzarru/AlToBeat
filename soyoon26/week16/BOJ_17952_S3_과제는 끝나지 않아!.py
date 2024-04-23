import sys
n = int(sys.stdin.readline().rstrip())
stack=[]
ans=0
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    if a[0] != 0:
        a[2]-=1
        if a[2]>0:
            stack.append(a)
        else:
            ans+=a[1]
    elif a[0]==0 and stack:
        stack[-1][2] -=1
        if stack[-1][2] == 0:
            ans+=stack[-1][1]
            stack.pop()
print(ans)