def solution(n, words):
    answer = []  # 사람 번호, 틀린 차례
    used = []
    order = 0
    for word in words:
        order += 1

        if word in used:
            order -= 1
            break
        else:
            if used:
                if used[order - 2][-1] == word[0]:
                    used.append(word)
                else:
                    order -= 1
                    break
            else:
                used.append(word)

    if words == used:
        answer = [0, 0]
    else:
        answer = [((order % n + 1)), ((order // n) + 1)]

    return answer