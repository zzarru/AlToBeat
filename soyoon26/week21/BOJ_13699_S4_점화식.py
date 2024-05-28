n = int(input())
nums=[1] + [0]*n
for i in range(1,n+1):
    for j in range(i):
        nums[i]+=nums[i-j-1]*nums[j]
print(nums[n])