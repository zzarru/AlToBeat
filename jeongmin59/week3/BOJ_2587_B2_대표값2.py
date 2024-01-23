# 2587_대표값2
'''
- 5개의 자연수가 주어질 때 평균과 중앙값 출력
'''

N = 5
lst = []

for _ in range(N):
    num = int(input())
    lst.append(num)

average = sum(lst)//5
median = sorted(lst)[2]

print(average)
print(median)
