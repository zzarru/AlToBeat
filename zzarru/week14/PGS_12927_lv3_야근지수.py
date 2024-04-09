'''
풀이 아이디어: works에서 가장 큰 값을 차례로 -1 해주면 최소화한 야근 피로도를 구할 수 있다.
1) works에서 가장 큰 값을 찾는다.
2) n회만큼 반복하면서 그 값을 -1 해준다.

조건
1) 남은 작업량 보다 남은 시간이 많은 경우를 고려해야한다.
'''


def solution(n, works):
    # 작업량 보다 남은 시간이 많은 경우
    if sum(works) < n:
        n = sum(works)

    for _ in range(n):
        idx = works.index(max(works))
        works[idx] -= 1

    fatigue = 0
    for work in works:
        fatigue += work ** 2

    return fatigue