import sys
N, L = map(int,sys.stdin.readline().split())
fruits = list(map(int,sys.stdin.readline().split()))
fruits.sort()

idx=0
while idx<len(fruits):
    if fruits[idx]<=L:
        L+=1
        idx+=1
    else:
        break
print(L)