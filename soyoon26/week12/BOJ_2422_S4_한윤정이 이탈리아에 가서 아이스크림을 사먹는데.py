import sys

N,M = map(int,sys.stdin.readline().split())
icecream=list(range(1,N+1))
ice_comb=int(N*(N-1)*(N-2)/6)
delete = list()
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    for j in icecream:
        if j != a and j != b:
            dl=[a,b,j]
            dl.sort()
            delete.append(tuple(dl))
sub=set(delete)
print(ice_comb-len(sub))
