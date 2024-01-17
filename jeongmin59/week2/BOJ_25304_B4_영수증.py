# 25304_영수증
'''
- 구매한 각 물건의 가격과 개수, 구매한 물건들의 총 금액
- 영수증에 적힌 총 금액과 일치하면 Yes, 아니면 No
'''

X = int(input())
N = int(input())
money = 0

for _ in range(N):
    a, b = map(int, input().split())

    money += (a * b)

if X == money:
    print('Yes')
else:
    print('No')
