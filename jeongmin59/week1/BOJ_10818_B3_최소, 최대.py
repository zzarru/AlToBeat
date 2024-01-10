# 10818_최소, 최대
'''
- N개 주어질 때, 최솟값과 최댓값 구하기
- min, max 함수 안 쓰고 풀어 보기
'''

N = int(input())
lst = list(map(int, input().split()))

min_cnt = lst[0]
max_cnt = lst[0]

for i in lst:
    if i < min_cnt:
        min_cnt = i
    if i > max_cnt:
        max_cnt = i

print(min_cnt, max_cnt)
