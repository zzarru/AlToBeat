n = int(input())
for _ in range(n):
    a,b=input().split()
    print('Distances: ',end="")
    for i in range(len(a)):
        ans = ord(b[i])-ord(a[i])
        if ans < 0:
            ans+=26
        print(ans,end=" ")
    print()