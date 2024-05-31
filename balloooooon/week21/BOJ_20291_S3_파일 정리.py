from collections import defaultdict
N = int(input())
format_dict = defaultdict(int)
for _ in range(N):
    name, format = input().split('.')
    format_dict[format] += 1

format_list = list(format_dict.keys())
format_list.sort()

for format in format_list:
    print(format, format_dict[format])