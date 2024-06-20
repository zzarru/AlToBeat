from itertools import permutations


def solution(k, dungeons):
    answer = 0
    lst = list(permutations(dungeons, len(dungeons)))
    for i in lst:
        cnt = 0
        test = k
        for j in i:
            if test >= j[0]:
                test -= j[1]
                cnt += 1
            else:
                break
        if cnt >= answer:
            answer = cnt

    return answer