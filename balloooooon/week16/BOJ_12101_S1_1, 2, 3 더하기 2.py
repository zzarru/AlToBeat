cnt=1
temp=[]
answer=[]
a, b=map(int,input().split())
def back(n,k):
    global cnt
    if n==k:
        if cnt==b:

            answer.append("+".join(temp))
            cnt += 1
            # print(answer)
            return 3
        else:
            cnt += 1
            return
    else:
        if cnt>b:
            return
        for i in range(1,4):
            if n+i<=k:
                temp.append(str(i))

                back(n+i,k)
                temp.pop()

back(0,a)

if answer:
    print(*answer)
else:
    print(-1)