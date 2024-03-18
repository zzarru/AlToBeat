#프로그래머스 lv1 크기가 작은 부분문자열

def solution(t, p):
    answer = 0
    
    # 몇 개씩 자를 것인지 정하기 위한 p의 길이
    p_length = len(p)
    
    temp = ''
    for i in range(len(t) - len(p) + 1):
        temp = t[i:i + len(p)]
        # 슬라이싱 한 값이 p 이하라면 answer 1 증가
        if int(temp) <= int(p):
            answer += 1
            
    return answer