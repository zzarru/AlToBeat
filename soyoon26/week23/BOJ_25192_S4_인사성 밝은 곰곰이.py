import sys
n = int(sys.stdin.readline().rstrip())
answer=0
cnt=[]
for _ in range(n):
    log = sys.stdin.readline().rstrip()
    if log == 'ENTER':
        count=set(cnt)
        answer+=len(count)
        cnt=[]
    else:
        cnt.append(log)
if cnt:
    cnt=set(cnt)
    answer+=len(cnt)
print(answer)