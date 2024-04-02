# PGS lv2 2022 KAKAO TECH INTERNSHIP 두 큐 합 같게 만들기

"""
처음에는 최악의 경우 탈출 조건을
list(q1) == queue1 or list(q2) == queue2
위와 같이 설정했었는데, queue에 있는 원소의 크기가 최대 1억이고
원소의 수가 최대 30만이라서 저렇게 하면 시간초과가 발생했다.
queue가 처음과 같아지는 순서가 큐의 길이*3이라서 그렇게 설정하니까 통과했다.

sum1, sum2를 while반복문이 실행될 때마다 sum메서드로 구했었는데,
원소의 갯수가 많고 숫자의 범위가 너무 커서 시간초과가 발생했다.
그래서 처음에 구한 sum1, sum2에 이동시킨 숫자를 빼고 더하는 것으로 수정했다.
"""

from collections import deque

def solution(queue1, queue2):  
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1, sum2 = sum(queue1), sum(queue2)
    answer = 0
    end = len(queue1) * 3
    while True:
        if sum1 == sum2:
            return answer
        
        if sum1 > sum2:
            q2.append(q1.popleft())
            sum1 -= q2[-1]
            sum2 += q2[-1]
        else:
            q1.append(q2.popleft())
            sum1 += q1[-1]
            sum2 -= q1[-1]
        answer += 1
            
        if answer >= end:
            return -1
        