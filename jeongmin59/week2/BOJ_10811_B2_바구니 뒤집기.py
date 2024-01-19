# 10811_바구니 뒤집기
'''
- 바구니의 순서를 어떻게 바꿀지 주어졌을 때, i번째 바구니부터 j번째 바구니의 순서를 역순으로 만듦
- 모든 순서를 바꾼 후, 가장 왼쪽 바구니부터 출력
'''

N, M = map(int, input().split())

basket = [n for n in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())

    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for b in basket:
    print(b, end=' ')
