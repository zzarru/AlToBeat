import sys
n = int(sys.stdin.readline().rstrip())
first = list(map(int,sys.stdin.readline().split()))
grow = list(map(int,sys.stdin.readline().split()))
total = 0
lst=[]
for i in range(n):
    lst.append([first[i],grow[i]])
lst.sort(key=lambda x : x[1])
for i in range(n):
    total += lst[i][0]+lst[i][1]*i
print(total)