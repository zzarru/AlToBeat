# 프로그래머스 달리기 경주

def solution(players, callings):
    
    # 선수 : 등수 딕셔너리 생성
    ranks = {player : i + 1 for i, player in enumerate(players)}
    
    # 등수 : 선수 딕셔너리 생성
    reversed_ranks = {value : key for key, value in ranks.items()}
    
    # 순위 변경을 순서대로 실행
    for calling in callings:
        # 추월할 선수의 현재 등수
        current = ranks[calling]
        # 추월당한 선수의 이름
        player = reversed_ranks[current - 1]
        # ranks에서 추월한 선수 등수 변경
        ranks[calling] -= 1
        # reversed_ranks에서 추월한 선수의 등수 변경
        reversed_ranks[current - 1] = calling
        # reversed_ranks에서 추월당한 선수의 등수 변경
        reversed_ranks[current] = player
        # ranks에서 추월당한 선수의 등수 변경
        ranks[player] = current
        
    # 모든 추월 종료 후 선수들 순서
    answer = list(reversed_ranks.values())
    return answer
