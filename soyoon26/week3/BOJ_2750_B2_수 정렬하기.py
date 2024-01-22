N = int(input())
num=list(set(int(input()) for _ in range(N)))

for i in range(len(num)-1,-1,-1):
    for j in range(i):
        if num[j] > num[j+1]:
            tmp = num[j]
            num[j] = num[j+1]
            num[j+1] = tmp
for j in num:
    print(j)

#버블정렬 