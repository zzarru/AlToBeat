# 처음에 두 리스트를 사용하여 두 곳모두 존재하는지만 확인하면 되는 쉬운 문제일줄 알았으나
# N, M은 500,000이하라는 경악스러운 조건에 의해 시간초과가 나오고 만다.
# 문제의 카테고리에 해쉬 테이블이 있어서 파이썬에서는 어떤식으로 활용할 수 있는지 확인해 보았는데
# 우리의 딕셔너리가 그 해쉬 테이블이라고 한다.
# 해쉬테이블은 O(1)의 시간복잡도를 가진다는 장점을 십분 이용하기로했다.
# 첫번째 리스트는 N개의 못 들은 사람을 key로 truthy한 value값으로 넣어서 딕셔너리로 재구성해주었고
# M개의 못 본 사람들이 key로 존재하는지 확인된 입력값을 두번째 리스트에 넣어주고 정렬해주었다

import sys
N, M = map(int,input().rstrip().split())
input = sys.stdin.readline

Not_hear = {}
hear_see = []

for i in range(N):
    somebody = input().rstrip()
    Not_hear[somebody] = 1

for i in range(M):
    somebody = input().rstrip()
    if somebody in Not_hear:
        hear_see.append(somebody)

hear_see.sort()
print(len(hear_see))
for i in range(len(hear_see)):
    print(hear_see[i])
