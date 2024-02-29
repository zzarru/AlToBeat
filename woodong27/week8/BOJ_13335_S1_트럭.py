# BOJ 13335 S1 트럭

from collections import deque

"""
현재 첫번째 트럭과 다리에 있는 트럭의 중량이
l 이하라면 첫번째 트럭을 넣어주고
아니라면 0을 넣어주면서 큐에서 pop과 append를 반복하면 된다.
"""

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))

bridge = deque([0] * w)
answer = 0
while trucks:
    bridge.popleft()
    answer += 1
    if sum(bridge) + trucks[0] <= l:
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)

while sum(bridge) != 0:
    answer += 1
    bridge.popleft()

print(answer)
