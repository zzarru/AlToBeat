# N개의 동방
N = int(input())

rooms = [1 for i in range(N)]

# 빌런의 행동 M
M = int(input())

# M번만큼 벽 허물기를 한다.
for _ in range(M):
    x, y = map(int, input().split())
    # x와 y의 범위에 있는 방들 중 벽이 있다면 허문다. (1->0으로 바꿈), 허물 때마다 방의 갯수를 -1해준다.
    for l in range(x, y):
        if rooms[l-1] != 0:
            rooms[l-1] = 0
            N -= 1

print(N)



