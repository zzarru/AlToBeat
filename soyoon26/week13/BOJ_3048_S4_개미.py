import sys
N1, N2 = map(int,sys.stdin.readline().split())
n1 = list(sys.stdin.readline().rstrip())
n1 = n1[-1::-1]
n2 = list(sys.stdin.readline().rstrip())
n=n1+n2
T= int(sys.stdin.readline().rstrip())

for i in range(T):
    for j in range(len(n)-1):
        if n[j] in n1 and n[j+1] in n2:
            n[j],n[j+1] = n[j+1],n[j]
            if n[j+1] == n1[-1]:
                break
print(*n,sep='')

