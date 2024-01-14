# 10813_공 바꾸기
'''
- N개의 바구니, M번 교환
- i번 바구니와 j번 바구니에 있는 공을 교환
- 순서대로 공을 교환할 때, 1번 바구니부터 N번 바구니에 들어있는 공의 번호 출력
'''

N, M = map(int, input().split())

lst = [0 for _ in range(N)]

cnt = 1
for x in range(N):
    lst[x] = cnt
    cnt += 1

for _ in range(M):
    i, j = map(int, input().split())

    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]

print(*lst)

'''
- 다른 풀이 (10~15번째 줄)

lst = [i for i in range(1, N+1)]

> 이런 방식으로 코드 줄이기 가능
'''
