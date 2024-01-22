n, K = map(int,input().split())
list = list(map(int,input().split()))
answer = [-1]
count = 0
for i in range(n-1,0,-1):
    for j in range(0,i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
            count += 1
            if count == K:
                answer = [list[j], list[j+1]]

print(*answer)