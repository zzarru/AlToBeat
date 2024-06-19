import sys
n = int(sys.stdin.readline().rstrip())
answer=0
for i in range(1,n+1):
    num = str(i)
    dif = 0
    for j in range(len(num)-1):
        if j == 0:
            dif = int(num[j])-int(num[j+1])
        else:
            diff = int(num[j])-int(num[j+1])
            if dif != diff:
                answer+=1
                break
print(n-answer)