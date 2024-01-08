# 10807_개수세기
'''
- n개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하기
'''

N = int(input())
lst = list(map(int, input().split()))
v = int(input())

ans = []

for i in lst:
    if i == v:
        ans.append(i)

print(len(ans))
