answer = [0,0]
for i in range(5):
    num = sum(list(map(int,input().split())))
    if num>answer[1]:
        answer[0],answer[1]=i+1,num
print(*answer)