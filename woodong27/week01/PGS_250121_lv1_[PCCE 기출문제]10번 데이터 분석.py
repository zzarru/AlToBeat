# 프로그래머스 [PCCE 기출문제]10번 데이터 분석

def solution(data, ext, val_ext, sort_by):
    answer = []
    
    # 분류 기준 확인
    key_index = 0
    if ext == 'date':
        key_index = 1
    elif ext == 'maximum':
        key_index = 2
    elif ext == 'remain':
        key_index = 3
        
    # 기준에 맞는 데이터만 answer에 추가
    for item in data:
        if item[key_index] < val_ext:
            answer.append(item)
            
    # answer를 sort_by를 기준으로 정렬
    sort_index = 0
    if sort_by == 'date':
        sort_index = 1
    elif sort_by == 'maximum':
        sort_index = 2
    elif sort_by == 'remain':
        sort_index = 3
    
    answer.sort(key = lambda x : x[sort_index])
    
    return answer
