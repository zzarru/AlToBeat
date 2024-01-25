num = list(input())

for end in range(1,len(num)):
    i = end
    while i > 0 and int(num[i-1])<int(num[i]):
        num[i],num[i-1] = int(num[i-1]),int(num[i])
        i-=1

print(*num,sep='')

#삽입정렬