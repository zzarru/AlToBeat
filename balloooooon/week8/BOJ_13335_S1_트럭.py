'''
트럭이 다리의 하중에 견딜만큼만 올라갈 수 있으며, 일방통행이다
그말은 그냥 무조건 여건이 된다면 인정 봐주지 말고 사정 봐주지 말고, 다리에 올리는 것이 최소시간이 된다.

큐의 길이가 곧 다리 길이로 생각하면 되고, 큐에 트럭을 appendleft, pop하는 것으로 이동시킨다

그래서 매초 1칸씩 이동하는 것은 큐에서 꺼내는 것으로 구현하고
만일 현재 다리가 다음 트럭을 투입하여도 하중을 견딘다면 trucks에서 다른 트럭을 큐에 넣고
다음 트럭을 투입할 수 없는 경우 이동만 시켜주는 의미로 0을 큐에 넣어주었다.

이 시뮬레이션은 모든 트럭이 pop되는 것을 목표로 하므로
pop될때마다 무게를 더해서 총 무게가 될때까지 돌아가도록 반복문을 완성했다.
'''

from collections import deque

n, w, L = map(int,input().split())
trucks = list(map(int,input().split()))
queue = deque([0 for i in range(w)])
goal = sum(trucks)
answer = 0
all_weight = 0

while all_weight < goal:
    all_weight += queue.pop()
    if trucks and trucks[0] + sum(queue) <= L:
        queue.appendleft(trucks.pop(0))
    else:
        queue.appendleft(0)
    answer += 1

print(answer)