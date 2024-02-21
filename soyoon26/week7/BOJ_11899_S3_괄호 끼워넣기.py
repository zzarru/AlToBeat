import sys
line=sys.stdin.readline().rstrip()
cnt=0
ans=0
for i in line:
    if i == '(':
        cnt+=1
    elif i == ')' and cnt <=0:
        ans+=1
    elif i ==')' and cnt >0:
        cnt-=1
print(cnt+ans)