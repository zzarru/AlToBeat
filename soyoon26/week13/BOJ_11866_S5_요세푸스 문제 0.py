import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())
deque = deque(range(1,N+1))
answer=[]

while deque:
    deque.rotate(-K+1)
    answer.append(deque.popleft())
print('<',end='')
print(*answer,sep=', ',end='>')