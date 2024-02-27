import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().split()))
#큐0 스택 1
B=deque(map(int,sys.stdin.readline().split()))
#i번 자료구조에 들어있는 원소
M=int(sys.stdin.readline().rstrip())
C=deque(map(int,sys.stdin.readline().split()))
#삽입할 수열
queue=deque()
for i in range(N):
    if A[i] == 0:
        queue.append(B[i])
answer=[]
while C:
    queue.appendleft(C.popleft())
    answer.append(queue.pop())
#for문 쓰기: C를 popleft할 필요가 없음
print(*answer,sep=' ')
#print(" ".join(map(str,result)))
