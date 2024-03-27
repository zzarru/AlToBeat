from itertools import combinations
import sys
N= int(sys.stdin.readline().rstrip())
ingred = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

ans= []
comb=[]
for i in range(1,N+1):
    cb=list((combinations(ingred, i)))
    for j in range(len(cb)):
        multi, sum = 1, 0
        for k in range(len(cb[j])):
            multi*=cb[j][k][0]
            sum+=cb[j][k][1]
        if multi >= sum:
            ans.append(multi - sum)
        else:
            ans.append(sum-multi)
print(min(ans))



