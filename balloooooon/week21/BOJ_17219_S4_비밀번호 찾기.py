n, tc = map(int,input().split())

site_dict = {}
for _ in range(n):
    site, password = input().split()
    site_dict[site] = password

for _ in range(tc):
    site = input()
    print(site_dict[site])