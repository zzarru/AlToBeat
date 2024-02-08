'''
V미터를 올라가는데 낮에는 A만큼 올라가고 밤에는 B만큼 미끄러진다.
정상에 오르기까지 걸리는 시간을 구하라.
'''

A, B, V = map(int, input().split())

day = (V - B) // (A - B)
if (V - B) % (A - B) != 0:
    day += 1

print(day)

# day = 0
# height = 0
# while height < V:
#     if height + A < V:
#         height = height + A - B
#         day +=1
#     else:
#         day += 1
#         break