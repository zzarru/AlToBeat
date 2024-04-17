import sys
n = int(sys.stdin.readline().rstrip())
start, end = 0,0
cnt=0
sum = 0
while end != n+1:
    if sum < n:
        end += 1
        sum+=end

    elif sum == n:
        end += 1
        sum += end
        cnt+=1
    elif sum > n:
        start += 1
        sum-=start


print(cnt)