import sys
n, m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

i,j=0,0
ans=[]
while i != n or j != m:
    if i == n:
        ans.append(b[j])
        j+=1
    elif j == m:
        ans.append(a[i])
        i+=1
    else:
        if a[i] > b[j]:
            ans.append(b[j])
            j+=1
        else:
            ans.append(a[i])
            i+=1
print(*ans)