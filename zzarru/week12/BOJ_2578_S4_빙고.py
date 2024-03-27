import sys
input = sys.stdin.readline

vertical_list = []
optical_list = []
cross_list = [[],[]]
for _ in range(5):
    vertical = list(map(int, input().split()))
    vertical_list.append(vertical)

for i in range(5):
    optical = []
    for j in range(5):
        optical.append(vertical_list[j][i])

        if i == j: #우하향 대각선
            cross_list[0].append(vertical_list[i][j])
        if i + j == 4: #좌하향 대각선
            cross_list[1].append(vertical_list[i][j])

    optical_list.append(optical)

# 숫자 부르기
cnt = 0
bingo = 0
for _ in range(5):
    numbers = list(map(int, (input().split())))
    for number in numbers:
        cnt += 1

        # 빙고 맞추기
        for verticals in vertical_list:
            if number in verticals:
                idx = verticals.index(number)
                verticals.pop(idx)
                vertical_len = len(verticals)
                if vertical_len == 0:
                    bingo += 1
                break

        if bingo == 3:
            print(cnt)
            sys.exit()

        for opticals in optical_list:
            if number in opticals:
                idx = opticals.index(number)
                opticals.pop(idx)
                optical_len = len(opticals)
                if optical_len == 0:
                    bingo += 1
                break

        if bingo == 3:
            print(cnt)
            sys.exit()

        if number in cross_list[0]:
            idx = cross_list[0].index(number)
            cross_list[0].pop(idx)
            cross1_len = len(cross_list[0])
            if cross1_len == 0:
                bingo += 1

        if number in cross_list[1]:
            idx = cross_list[1].index(number)
            cross_list[1].pop(idx)
            cross2_len = len(cross_list[1])
            if cross2_len == 0:
                bingo += 1

        if bingo == 3:
            print(cnt)
            sys.exit()