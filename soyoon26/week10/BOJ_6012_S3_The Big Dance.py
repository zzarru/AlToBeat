import sys
N=int(sys.stdin.readline().rstrip())
nums=list(range(1,N+1))
cnt=[]
def rose(lst):
    global cnt
    m=len(lst)
    if m == 2:
        cnt.append(lst[0]*lst[1])
        return cnt
    if m == 3:
        cnt.append(lst[0]*lst[1])
        return cnt
    if m%2:
        rose(lst[:m//2+1])
        rose(lst[m//2+1:])
    else:
        rose(lst[:m//2])
        rose(lst[m//2:])
rose(nums)
print(sum(cnt))