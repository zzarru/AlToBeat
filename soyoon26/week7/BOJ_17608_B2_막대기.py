import sys
N=int(input())
stack=[]
for i in range(N):
    n=int(sys.stdin.readline().rstrip())
    stack.append(n)
max=max(stack)
cnt=1
end=stack.pop()
while end!=max:
    if stack[-1] > end:
        cnt+=1
        end=stack.pop()
    else:
        stack.pop()
print(cnt)
