from collections import defaultdict
str_dict = defaultdict(int)

N = int(input())
for _ in range(N):
    temp, value = input().split()
    str_dict[temp] += int(value)

str_list = list(str_dict.keys())
str_list.sort(key= lambda x:(len(x),x))
for s in str_list:
    print(s,str_dict[s])
