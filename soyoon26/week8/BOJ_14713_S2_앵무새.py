import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
S=[]
for i in range(N):
    s=deque()
    queue=deque(sys.stdin.readline().split())
    S.append(queue)
line=deque(sys.stdin.readline().split())
answer='Possible'
while line:
    cnt=0
    for j in range(N):
        if S[j] and line and S[j][0] == line[0]:
            line.popleft()
            S[j].popleft()
        else:
            cnt+=1
    if cnt == N:
        answer='Impossible'
        break
for k in range(N):
    if len(S[k]) > 0:
        answer='Impossible'
print(answer)
