# 2738_행렬 덧셈
'''
- N * M 크기의 두 행렬 A와 B가 주어졌을 때 더한 행렬 출력
'''

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        answer = A[i][j] + B[i][j]
        print(answer, end=' ')
    print()
