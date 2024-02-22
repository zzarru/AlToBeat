import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    stack.append(int(input()))

stack.sort()

for i in stack:
    print(i)