from collections import defaultdict
num_dict = defaultdict(int)
N = int(input())
num_list = list(map(int,input().split()))
for num in num_list:
    num_dict[num] += 1

M = int(input())
answer = []
temp = list(map(int,input().split()))
for i in temp:
    answer.append(num_dict[i])
print(*answer)