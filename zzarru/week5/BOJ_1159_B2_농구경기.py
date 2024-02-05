N = int(input()) # 선수의 숫자

players = [] # 각 선수의 첫 글자
for _ in range(N):
    first_alph = input()[0]
    players.append(first_alph)

alphabets = []
selected_players = []
for player in players:
    if player not in alphabets: # for문 중복을 방지하기 위하여
        alphabets.append(player)
        number_of_player = players.count(player)

        if number_of_player > 4:
            selected_players.append(player)

selected_players.sort() # 사전 순으로 정렬한다.

if len(selected_players) == 0:
    print('PREDAJA')

else:
    print(*selected_players, sep='')