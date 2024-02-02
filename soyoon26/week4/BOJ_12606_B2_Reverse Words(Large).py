T = int(input())
for t in range(1,T+1):
    line = input().split()
    line.reverse()
    print(f'Case #{t}:',*line)