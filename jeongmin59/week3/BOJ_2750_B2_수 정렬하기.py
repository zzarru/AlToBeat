# 2750_수 정렬하기
'''
- N개의 수가 주어졌을 때 오름차순으로 정렬
'''

N = int(input())
lst = []

for _ in range(N):
    num = int(input())
    lst.append(num)

# 버블 정렬
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for x in lst:
    print(x)
