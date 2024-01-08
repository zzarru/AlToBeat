N = int(input())
nums = list(map(int, input().split()))
v = int(input())

cnt = 0
for n in nums:
    if n == v:
        cnt += 1
print(cnt)