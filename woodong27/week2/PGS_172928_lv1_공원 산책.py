# 프로그래머스 lv1 공원 산책

# 동 서 남 북 이동 위치 딕셔너리
direction_to_index = {'N' : 2, 'E' : 1, 'S' : 3, 'W' : 0}
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def solution(park, routes):
    answer = []
    
    # 공원의 한 변 길이
    col, row = len(park), len(park[0])
    
    # 이동 시작 위치
    si, sj = 0, 0
    
    # 2차원 배열을 조회해서 시작 위치를 찾아서 기록한다.
    for i in range(col):
        for j in range(row):
            if park[i][j] == 'S':
                si, sj = i, j
    
    # 순서대로 이동
    for route in routes:
        direction, amount = route.split(' ')
        idx = direction_to_index[direction]
        # 이동 횟수 만큼 한 칸씩 이동
        for i in range(1, int(amount) + 1):
            ni, nj = si + di[idx] * i, sj + dj[idx] * i
            # 만약 다음 칸이 공원의 범위 안에 있고, 장애물이 없을 경우
            if 0 <= ni < col and 0 <= nj < row and park[ni][nj] != 'X':
                # 마지막 이동이라면 이동한 경로를 저장해준다.
                if i == int(amount):
                    si, sj = ni, nj
                continue
            # 다음 칸에 장애물이 있거나, 공원의 범위 밖이면 이동을 해당 이동을 하지 않는다.
            else:
                break
    
    # 최종적으로 이동을 완료한 위치를 기록한다.
    answer = [si, sj]
    return answer