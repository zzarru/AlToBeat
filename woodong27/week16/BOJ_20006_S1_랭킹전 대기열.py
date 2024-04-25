# BOJ 20006 S1 랭킹전 대기열

"""
그냥 문제에서 주어진 조건대로 조건문을 구성하고
새 멤버가 들어올 때 마다 반복하면 된다.
"""

p, m = map(int, input().split())


def matching(level, name):
    for room in rooms:
        if len(room) < m:
            if room[0][1] - 10 <= level <= room[0][1] + 10:
                room.append((name, level))
                return

    rooms.append([(name, level)])


rooms = []
for _ in range(p):
    level, name = input().split()
    level = int(level)

    matching(level, name)


for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    room.sort(key=lambda x: x[0])
    for name, level in room:
        print(level, name)
