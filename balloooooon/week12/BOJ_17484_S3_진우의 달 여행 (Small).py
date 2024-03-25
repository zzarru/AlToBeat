'''
완전탐색을 쓰고싶었으나, 재귀로 방향을 바꿨습니다.
'''


m, n = map(int,input().split())
graph = []
for _ in range(m):
    temp = list(map(int,input().split()))
    graph.append(temp)

di = [1,1,1]
dj = [-1,0,1]
answer = []

def move(row, col, ex_dir, life, score):
    if life == 0:
        answer.append(score)
        return
    dir = [0, 1, 2]

    for k in dir:
        if k != ex_dir:
            ni = row + di[k]
            nj = col + dj[k]
            if 0 <= ni < m and 0 <= nj < n:
                move(ni, nj, k, life - 1, score + graph[ni][nj])

for j in range(n):
    for dir in range(3):
        move(0, j, dir , m-1 ,graph[0][j])

print(min(answer))