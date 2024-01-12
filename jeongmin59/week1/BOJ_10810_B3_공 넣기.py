# 10810_공 넣기
'''
- i번 바구니부터 j번 바구니까지 k번 번호가 적혀져 있는 공을 넣음
- 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 넣음
- 각 바구니에 어떤 공이 들어 있는지 출력
'''

N, M = map(int, input().split())

lst = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())

    for x in range(i-1, j):
        lst[x] = k

print(*lst)
