def solution(score):
    # 1 idx와 함께 합계 저장
    total_dic = {}
    idx = 0
    for s in score:
        total_dic[idx] = sum(s)
        idx += 1

    # 2 값을 가지고 정렬
    total_sorted = sorted(total_dic.items(), key=lambda item: item[1], reverse=True)

    # 3 등수 매기기
    num_before = -1  # 이전 값 저장해서 같은 값인지 비교하기
    rank = 0  # 순위
    cnt = 0  # 중복 등수 있을 경우 패스하는 카운트
    rank_dic = {}
    for total in total_sorted:
        if num_before != total[1]:
            rank = rank + cnt + 1
            num_before = total[1]
            rank_dic[total[0]] = rank
            cnt = 0

        else:
            rank_dic[total[0]] = rank
            cnt += 1

    # 4 key 값으로 정렬하기
    sorted_rank = sorted(rank_dic.items(), key=lambda item: item[0])

    # 5 값 출력하기
    answer = []
    for ans in sorted_rank:
        answer.append(ans[1])
    return answer