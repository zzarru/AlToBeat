# BOJ 16234 G4 인구 이동

"""
인구 이동이 불가능 할 때까지 계속 해야 하기 때문에
while 반복문을 사용해서 매 인구이동마다 결과를 체크해서
반복문의 탈출 조건을 확인한다.
아직 방문하거나 bfs를 시작하지 않은 지역이면서
주변 지역과의 인구수 차이가 l 이상 r 이하라면 인구이동 가능한 지역으로 묶어준다.

각 날짜마다 인구이동이 가능하도록 묶이는 지역이 여러개 일 수 있다는 것을 고려해야 한다.
"""

from collections import deque


def moving(si, sj):
    q = deque([(si, sj)])
    union = [(si, sj)]
    while q:
        ci, cj = q.popleft()
        for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if l <= abs(populations[ni][nj] - populations[ci][cj]) <= r:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    union.append((ni, nj))

    return union


n, l, r = map(int, input().split())

populations = [list(map(int, input().split()))for _ in range(n)]

answer = 0
while True:
    flag = 0
    visited = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                union_country = moving(i, j)

                if len(union_country) > 1:
                    flag = 1
                    union_population = sum(populations[ui][uj] for ui, uj in union_country) // len(union_country)
                    for ui, uj in union_country:
                        populations[ui][uj] = union_population

    if not flag:
        break

    answer += 1

print(answer)
