import  sys
x, y = sys.stdin.readline().split()
numx, numy= int(x[-1::-1]),int(y[-1::-1])
ans=str(numx+numy)
print(int(ans[-1::-1]))