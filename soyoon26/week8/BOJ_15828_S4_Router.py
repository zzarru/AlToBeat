from collections import deque
import sys
N=int(sys.stdin.readline().rstrip())
router=deque()
while True:
    packet=int(sys.stdin.readline().rstrip())
    if packet != 0 and packet != -1 and len(router)<N:
        router.append(packet)
    elif router and packet==0:
        router.popleft()
    elif packet == -1:
        break
if router:
    print(' '.join(map(str,router)))
else:
    print('empty')
