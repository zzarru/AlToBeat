import sys
a,p=map(int,sys.stdin.readline().split())
visited=[0]*(250000)
def pownum(a,p):
    num=str(a)
    res=0
    for n in num:
        res+=pow(int(n),p)
    return res
cnt=0
def renum(num,p):
    global cnt
    if visited[num] != 0:
        return visited[num]-1
    else:
        cnt+=1
        visited[num] = cnt
        return renum(pownum(num,p),p)
print(renum(a,p))