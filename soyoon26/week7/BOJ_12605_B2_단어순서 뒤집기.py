import sys
N=int(sys.stdin.readline().rstrip())
for i in range(N):
    line=list(sys.stdin.readline().split())
    print(f'Case #{i+1}:',*line[::-1])