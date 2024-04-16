import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip()) 
ingredient = list(map(int,sys.stdin.readline().split()))
ingredient.sort()
start, end = 0, n-1
cnt = 0
while start < end:
    if ingredient[start]+ingredient[end] == m:
        cnt+=1
        start+=1
        end-=1
    elif ingredient[start]+ingredient[end] < m :
        start += 1
    elif ingredient[start]+ingredient[end] > m :
        end -= 1
print(cnt)
