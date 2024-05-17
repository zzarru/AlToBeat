hour, minutes = map(int, input().split())
needed = int(input())

finished = (hour * 60) + minutes + needed
if finished >= 1440:
    finished -= 1440
    print(finished // 60, finished % 60)

else:
    print(finished // 60, finished % 60)