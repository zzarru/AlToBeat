'''
난 솔직히 이문제 이해는 안된다.
문제 풀이 영상을 다수 찾아봤는데, 거기서 느낀 감상은
해리포터에서 아브라카다브라라는 주문을 외쳐야 상대방이 죽는데
문제 풀이영상은 상대방에게 죽어라 외치는 것만으로 상대방을 죽이게 만드는
그냥 말하는대로 된다는 느낌이다

하노이 원리는 알아먹겠는데, 코드로 구현한거 보면 와닿지가 않는다.

'''


cnt = 0
n = int(input())
def hanoi(n, start, temp, goal):
    global cnt

    if n == 1:
        cnt += 1
        print(start, goal)
        return

    hanoi(n-1, start, goal, temp) # 가장 큰 원판을 옮기기위해 보조 기둥으로 n-1개를 모두 이사
    print(start, goal) # 가장 큰 원판을 목표 기둥으로 옮긴다.
    cnt += 1
    hanoi(n-1, temp, start, goal ) # 보조 기둥에 옮겨놨던 n-1개의 원판을 목표기둥으로 옮긴다.
    return
print(2**n-1)
hanoi(n,1,2,3)
