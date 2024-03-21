'''
*구명보트에는 한번에 최대 2명만 탈 수 있다.
1) people 배열을 몸무게 순으로 정렬한다.
2) 가장 몸무게가 많이 나가는 사람(bigbro)과 가장 적게 나가는 사람(smallbro)의 무게를 합하여 limit보다 적거나 같다면 두 사람을 함께 보트에 태운다.
3) limit보다 크다면 가장 몸무게가 많이 나가는 사람 혼자 보트에 태워보낸다.
4) 태워보낼 때마다 boat +1 해준다.
'''

def solution(people, limit):
    boat = 0 #탈출에 필요한 구명보트 최소 개수
    people.sort() #체중이 적게 나가는 순으로 정렬

    smallbro, bigbro = 0, len(people)-1

    while smallbro <= bigbro:
        if people[smallbro] + people[bigbro] <= limit:
            smallbro += 1
        bigbro -= 1
        boat += 1

    return boat