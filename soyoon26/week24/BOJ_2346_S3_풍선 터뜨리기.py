from collections import deque, defaultdict
import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().split()))
number = deque((i+1,nums[i]) for i in range(n))
ans = []

while number:
    turn = number.popleft()
    print(turn[0],end=" ")
    if turn[1] > 0:
        number.rotate(-turn[1]+1)
    else:
        number.rotate(-turn[1])

