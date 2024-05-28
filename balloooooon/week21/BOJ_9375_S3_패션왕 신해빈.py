'''
옷을 단하나라도 걸치도록 만드는 것이 핵심
기본적인 경우의 수로 생각해서
모자가 3가지 윗옷이 4가지 아랫옷이 3가지라면
모든 경우의수가 3*4*3일 것이다
하지만 모자를 안 썼을 때도, 상의을 안 입었을 때도, 하의를 안 입은것도 패션아닌가?
(이해를 위해 조금 의미를 부여해봤다.)
그러면 각 가짓수가 1개씩 더해진다
이 문제가 그러한 문제이다 안 입은것도 패션이다...
이렇게하면 모든 걸치지않은 알몸패션도 탄생하므로 해당 가짓수를 마지막에 빼주면된다.
'''

from collections import defaultdict

tc = int(input())
for _ in range(tc):
    clothes_dict = defaultdict(list)
    n = int(input())
    temp = 1

    for _ in range(n):
        name, category = input().split()
        clothes_dict[category].append(name)
    for category in clothes_dict:
        temp *= (len(clothes_dict[category])+1)
    answer = temp - 1
    print(answer)

