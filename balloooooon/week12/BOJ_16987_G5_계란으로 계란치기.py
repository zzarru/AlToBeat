'''

풀면서 애를 많이 먹었다.
백트래킹을 했고, 인자로 달걀들의 상황을 리스트로 전달했다.
매번 박치기 대결을 할때 달걀들의 상태를 갱신해주었고 재귀할때마다 답을 최신화해주었다.
최신화해준이유는 어떤 특수한 경우에 대해 오답이 나온다.
예를들어 1번과 3번달걀이 박았고, 2번달걀이 박으려하는데 박을 상대가 없어서 함수가
일찍 종료가 된다. 그냥 반복문이 안돌아서... 그런데 이함수의 정상적인 종료조건은 마지막 달걀차례가
끝나서 끝나야하는데, 방금말한 경우를 빠뜨리게 되므로 답변을 최신화하는것으로 케어했다.

'''

N = int(input())
eggs= [list(map(int,input().split())) for _ in range(N) ]
#내구도와 무게
answer = 0

def egg_fight(broken_eggs, home_team, cur_broken):
    global answer
    answer = max(answer, cur_broken) #만에 하나의 경우의 수가 여기에 해당했다.
    if home_team == N:
        answer = max(answer, cur_broken)
        return
    if broken_eggs[home_team][0]<=0:
        egg_fight(broken_eggs, home_team + 1, cur_broken)
        return
    for away_team in range(0,N):
        if away_team == home_team:
            continue

        if broken_eggs[away_team][0] > 0 and broken_eggs[home_team][0] > 0:

            broken_point = 0

            broken_eggs[away_team][0] -= broken_eggs[home_team][1]
            if broken_eggs[away_team][0] <= 0:
                broken_point += 1

            broken_eggs[home_team][0] -= broken_eggs[away_team][1]
            if broken_eggs[home_team][0] <= 0:
                broken_point += 1

            egg_fight(broken_eggs, home_team + 1, cur_broken + broken_point)

            broken_eggs[away_team][0] += broken_eggs[home_team][1]
            broken_eggs[home_team][0] += broken_eggs[away_team][1]
egg_fight(eggs, 0, 0)

print(answer)