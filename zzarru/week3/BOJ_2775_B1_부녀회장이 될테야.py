T = int(input()) # 테스트 케이스의 개수

for _ in range(T): # 테스트 케이스만큼 반복
    # k층의 n호에 사는 사람의 수를 구하라
    k = int(input())
    n = int(input())

    apt = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]] # 0층의 세대 구성

    for floor in range(k): # k층까지 모든 호수의 사람을 채워넣자
        story = [] #각 층의 호들
        family = 0
        for room in apt[floor]: # 아래층의 각 세대별 수
            family += room # k층의 n호는 (k-1)층의 1호 ~ n호를 더한 값이다
            story.append(family) # 각 층의 세대원 수를 채워 넣는다.

        apt.append(story) # 완성된 해당 층을 아파트 리스트에 넣는다. 리스트의 idx가 층수와 같다.

    print(apt[k][n-1])
