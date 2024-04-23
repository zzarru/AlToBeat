N = int(input())
for _ in range(N):

    x = 0
    y = 0
    cnt = 0

    x_list = [0]
    y_list = [0]

    dx = [0,1,0,-1] #우회전시 여기서 인덱스를 +1, 좌회전시는 -1
    dy = [1,0,-1,0]
    conditions = list(input())
    for condition in conditions:
        mode = cnt % 4
        if condition == 'R':
            cnt += 1
        elif condition == 'L':
            cnt -= 1
        elif condition == 'F':
            x += dx[mode]
            y += dy[mode]
        else:
            x -= dx[mode]
            y -= dy[mode]
        x_list.append(x)
        y_list.append(y)
    answer = abs(max(x_list)-min(x_list)) * abs(max(y_list) - min(y_list)) #사각형의 넓이
    print(answer)