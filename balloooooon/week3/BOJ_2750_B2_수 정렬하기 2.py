N = int(input())
num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)
num_list.sort()

for i in range(N):
    print(num_list[i])
