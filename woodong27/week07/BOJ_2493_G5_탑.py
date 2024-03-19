# BOJ 2493 G5 탑

"""
레이저가 왼쪽으로 발사되기 때문에 반복문을 역순으로 수행한다.
현재보다 더 큰 탑을 만나지 않으면 계속 stack에 넣어주고
더 큰 탑을 만나게 되면, 여태까지 stack에 들어갔던 탑들에 대해서
레이저를 수신하였는지 확인해준다.
"""

n = int(input())
towers = list(map(int, input().split()))

answer = [0] * n
stack = [n-1]

for i in range(n-1, -1, -1):
    while stack and towers[i] > towers[stack[-1]]:
        answer[stack.pop()] = i + 1
    stack.append(i)

print(*answer, sep=" ")
