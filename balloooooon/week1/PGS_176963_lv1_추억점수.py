# 해당 문제는 photo라는 리스트에 각 개인이 회상하는 사진속 인물을 리스트 정보로 담아두었고
# 해당 정보가 name이라는 진짜 정보랑 얼마나 일치하는지 알아보는 문제이다
# 일치하면 yearning에서 가중치를 들고와서 점수를 매기는데 이를 편하게하기위해서
# 딕셔너리를 활용해서 name을 key로 yearning을 value로 둬서 가중치를 더하기 편하게 만들었다

def solution(name, yearning, photo):
    dict_photo_score = dict(zip(name, yearning))
    answer = []
    for photo_list in photo:
        temp = 0
        for photos in photo_list:
            if photos in name:
                temp += dict_photo_score[photos]
        answer.append(temp)
    return answer