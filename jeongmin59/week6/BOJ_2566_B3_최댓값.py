# 2566_최댓값
'''
- 9 * 9 크기의 격자판이 주어졌을 때, 최댓값을 찾고 최댓값이 몇 행 몇 열에 위치했는지 출력
'''

N = 9
lst = [list(map(int, input().split())) for _ in range(N)]

maxV = 0
row = 0
col = 0

for i in range(N):
    for j in range(N):
        if maxV <= lst[i][j]:
            maxV = lst[i][j]
            row = i+1
            col = j+1

print(maxV)
print(row, col)

