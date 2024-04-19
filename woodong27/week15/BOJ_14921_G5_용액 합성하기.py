# BOJ 14921 G5 용액 합성하기

"""
answer = min(abs(answer), abs(temp)) 
이렇게 하면 안된다.
가장 0에 가까운 결과를 출력하는거라 음수가 나올 수도 있기 때문

두 수의 합이 0보다 작으면 start를 1 늘려서 합한 값이 더 커지게 하고
0보다 크면 end를 감소시켜서 합이 더 작아지게 만든다.
"""

n = int(input())
solutions = list(map(int, input().split()))

start, end = 0, n - 1
answer = solutions[start] + solutions[end]
while end > start:
    temp = solutions[start] + solutions[end]
    if abs(temp) < abs(answer):
        answer = temp
    if temp < 0:
        start += 1
    else:
        end -= 1

print(answer)
