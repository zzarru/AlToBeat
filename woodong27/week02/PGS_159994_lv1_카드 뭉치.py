# 프로그래머스 lv1 카드 뭉치

def solution(cards1, cards2, goal):
    answer = ''
    
    # 임시로 문자를 저장할 리스트
    temp = []
    # goal의 단어들을 하나씩 돌아가며 cards1과 cards2의 가장 앞 단어와 동일한지 검사한다.
    # 검사해서 동일하다면 가장 앞 단어를 제거해서 다음에 중복되지 않게 한다.
    for word in goal:
        if cards1 and word == cards1[0]:
            temp.append(cards1.pop(0))
        elif cards2 and word == cards2[0]:
            temp.append(cards2.pop(0))
            
    if ''.join(temp) == ''.join(goal):
        answer = 'Yes'
    else:
        answer = 'No'
    
    return answer