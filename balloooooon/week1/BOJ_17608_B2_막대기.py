N = int(input())
temp = []
for i in range(N):
    num = int(input())
    temp.append(num)
wall_list = temp[::-1]
answer = 1
standard = wall_list[0]
for wall in wall_list:
    if wall > standard:
        standard = wall
        answer += 1
print(answer)