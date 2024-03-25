# BOJ 15686 G5 치킨 배달

"""
치킨집과 집들의 목록을 구한 뒤
치킨집들을 순서대로 골라가며 m개만큼 골랐을 때
각 집들과의 치킨거리 합을 구하고
최소값인지 비교하면 된다.
"""

n, m = map(int, input().split())
city = [list(map(int, input().split()))for _ in range(n)]


def chicken_delivery(selected_chicken, current):
    global answer
    if len(selected_chicken) == m:
        temp = 0
        for hi, hj in houses:
            distance = n * 2  # 거리 비교를 위해 최악의 경우 사용
            for ci, cj in selected_chicken:
                distance = min(abs(hi - ci) + abs(hj - cj), distance)
            temp += distance
        answer = min(temp, answer)
        return

    for idx in range(current, len(chickens)):
        selected_chicken.append(chickens[idx])
        chicken_delivery(selected_chicken, idx + 1)
        selected_chicken.pop()


houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chickens.append((i, j))
        elif city[i][j] == 1:
            houses.append((i, j))


answer = n * 2 * len(houses)  # 최악의 경우(모든 집들의 치킨 거리가 최대)
for i in range(len(chickens)):
    chicken_delivery([chickens[i]], i)

print(answer)
