# 10871_X보다 작은 수
'''
- N개로 이루어진 수열 A와 정수 X가 주어질때, A에서 X보다 작은 수 모두 출력
'''

N, X = map(int, input().split())
lst = list(map(int, input().split()))

ans = []

for i in lst:
    if i < X:
        ans.append(i)

print(*ans)
