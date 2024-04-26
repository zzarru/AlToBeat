N, T = map(int,input().split())

order_list = [ list(input().split()) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]
dir = 0
x = 0
y = 0
temp = 0 # 이전에 운전한 시각(time)을 저장
for time, mode in order_list: # 어느 시각'에'(time)
    sec = int(time) - temp # 몇 초'동안'(sec) 운전하는지
    x += dx[dir] * sec
    y += dy[dir] * sec
    if mode == 'right':
        dir = (dir+1)%4
    else:
        dir = (dir-1)%4
    temp = int(time)
    T -= sec

x += dx[dir] * T
y += dy[dir] * T

print(x,y)