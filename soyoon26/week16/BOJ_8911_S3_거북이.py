import sys
t=int(sys.stdin.readline().rstrip())
dx=[0,-1,0,1] # 좌우
dy=[1,0,-1,0] #위아래
for _ in range(t):
    turtle = list(sys.stdin.readline().rstrip())
    idx = 0
    min_x,max_x,min_y,max_y=0,0,0,0
    x,y=0,0
    for i in turtle:
        if i == 'F':
            x+=dx[idx]
            y+=dy[idx]
        elif i == 'B':
            x-=dx[idx]
            y-=dy[idx]
        elif i == 'L':
            idx = (idx+1)%4
        elif i == 'R':
            idx = (idx+3)%4
        min_x = min(min_x,x)
        max_x = max(max_x,x)
        min_y = min(min_y,y)
        max_y = max(max_y,y)
    print(abs(max_x-min_x)*(max_y-min_y))


