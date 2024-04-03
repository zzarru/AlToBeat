# BOJ 14719 G5 빗물

"""
자신보다 더 큰 높이가 좌, 우에 있다면
빗물이 고일 수 있다.
처음과 가장 마지막 칸에는 빗물이 쌓일 수 없기 때문에
첫번째 부터 w-1 까지 반복하면서
고이는 빗물의 값을 더해주면 된다.
"""

h, w = map(int, input().split())
heights = list(map(int, input().split()))

answer = 0
for i in range(1, w-1):
    left = max(heights[:i])
    right = max(heights[i:])
    min_value = min(left, right)

    if min_value > heights[i]:
        answer += min_value - heights[i]

print(answer)
