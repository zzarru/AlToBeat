# 달팽이순열, 행렬을 +10 +8 -8 -6 +6 +4 -4 -2 +2
# 이런식으로 일정한 규칙성을 통해서 뱅뱅뱅 돌아가듯이 구현을 해야한다.
# 그래서 기억해야할 것은 아래로 내려가고 우측으로 가는 구간은 +로
# 위로 올라가고 좌측으로 가는 구간은 -로 하기위해서 k라는 변수를 통해서
# 스위치를 껐다, 켰다한다고 생각하면될 듯 하다.
N=int(input())
if N>1:
    m = (N - 1) * 4 + 3 #횅
    n = (N - 1) * 4 + 1 #열

    row = m
    col = n
    graph = [[' ' for i in range(n + 1)] for j in range(m)]

    graph[0] = ['*'] * n # 첫째행은 구현의 귀찮음으로 그냥 패스
    x=y=0
    k=1
    while 1:
        for i in range(m-1):
            x += k
            graph[x][y] ='*'

        for j in range(n-1):
            y += k
            graph[x][y] = '*'

        k *= -1
        m -= 2
        n -= 2
        if m-1 == 0: # 다 그렸으면 빠져나오기위해 컷
            break
# 구현은 여기서 끝인데 출력하는게 '문제에서 요구하는대로'이기때문에
# 첫트라이에서 각 행마다 마지막에 빈칸으로 된 열이 추가로 필요함을 인지
# 두번째트라이에서 마지막 행에선 마지막 빈칸이 없음을 인지
# 마지막 트라이에서 두번째 행엔 빈칸이 특이하게 됨을 인지
# 구현은 여차저차 해냈는데, 출력에 대해서 이렇게 다양한 시행착오를 겪었다
# 어떻게 보면 이번 주의 주제에 가장 맞는 취지의 문제를 푼 것 같다

    for i in range(row):
        if i < row-1:
            if i != 1:
                print(*graph[i], sep='')
            else:
                print(*graph[i][0], end ='')
                print(*graph[i][1])

        else:
            for j in range(col):
                print(*graph[i][j], end='')
else:
    print('*', end ='')