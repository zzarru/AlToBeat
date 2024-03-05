import sys
#p=1
T=int(input())
for t in range(T):
    a,b=map(int,sys.stdin.readline().split())
    while a != b:
        if a > b:
            a=a//2
        else:
            b=b//2
    print(a*10)
