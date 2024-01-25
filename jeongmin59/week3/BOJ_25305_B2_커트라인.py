# 25305_커트라인
'''
- 응시자의 수 N과 상 받는 수 k가 주어짐
- 상 받는 사람들 중 가장 낮은 사람 점수 출력
'''

N, k = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
print(lst[k-1])
