num = list(map(int,input().split()))
for i in range(len(num)):
    max_idx=i
    for j in range(i+1,len(num)):
        if num[max_idx] < num[j]:
            max_idx = j
    num[max_idx],num[i]=num[i],num[max_idx]
print(num[1])
#선택정렬