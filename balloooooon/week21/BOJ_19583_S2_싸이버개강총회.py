import sys
from collections import defaultdict

attendance = defaultdict(int)
answer = {}
def twenty_four(time):
    return int(time[:2]) * 60 + int(time[3:])

bb, bs, bf = input().split()

bb = twenty_four(bb)
bs = twenty_four(bs)
bf = twenty_four(bf)


bb_dict = {}
# sys.stdin은 남은 input들

for line in sys.stdin:
    time, name = line.split()
    time = twenty_four(time)
    if time <= bb:
        attendance[name] = 1
    elif bs <= time <= bf:
        if name in attendance:
            answer[name] = 1
    else:
        continue
print(len(answer))
