import sys
K=int(sys.stdin.readline().rstrip())
nums=[]
for i in range(K):
    num=int(sys.stdin.readline().rstrip())
    if num != 0:
        nums.append(num)
    else:
        nums.pop()
print(sum(nums))

